import os
import uuid
import json
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from dotenv import load_dotenv, set_key
import chromadb
from chromadb.utils import embedding_functions
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage # SystemMessage might be used by agents
from langchain_community.chat_message_histories import ChatMessageHistory # Updated import
from langchain_core.runnables.history import RunnableWithMessageHistory

# --- Import tools and agents from submodules ---
# Changed to direct imports assuming main.py is run from langchain_server directory
from tools.erpnext_tools import erpnext_tools_list, make_erpnext_request
from tools.web_tools import web_tools_list
# Import all tools directly for the /invoke_tool endpoint
from tools.erpnext_tools import erpnext_get_doctype_structure, erpnext_get_document, erpnext_create_document, erpnext_update_document, erpnext_delete_document, erpnext_execute_method
from tools.web_tools import google_custom_search, scrape_website_to_markdown

from agents.routing_agent import routing_agent_executor, all_tools as routing_agent_tools
from agents.data_retrieval_agent import data_retrieval_agent_executor, data_retrieval_tools


# --- Combine all tools for potential direct invocation ---
# Create a dictionary for easy lookup by name
available_tools_map = {tool.name: tool for tool in routing_agent_tools} # routing_agent_tools contains all tools

# --- Load and Manage Environment Variables ---
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

if not os.path.exists(dotenv_path):
    print(f"Warning: .env file not found at {dotenv_path}. Creating a template .env file.")
    with open(dotenv_path, 'w') as f:
        f.write("# Environment variables for HRMS AI Agents app\n")
        f.write("LANGCHAIN_API_KEY=\n")
        # The user mentioned they will handle the Gemini key, so keep placeholder or let them manage it.
        f.write("GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE\n")
        f.write("CHROMA_DB_PATH=./langchain_server/chroma_db_data\n")
        f.write("VECTOR_DB_COLLECTION_PREFIX=hrms_conv_\n")
        f.write("ERPNext_API_URL=http://your_erpnext_instance_url:8000\n")
        f.write("ERPNext_API_KEY=YOUR_ERPNext_API_KEY\n")
        f.write("ERPNext_API_SECRET=YOUR_ERPNext_API_SECRET\n")
        f.write("GOOGLE_SEARCH_API_KEY=YOUR_GOOGLE_SEARCH_API_KEY\n")
        f.write("GOOGLE_CSE_ID=YOUR_GOOGLE_CSE_ID\n")

load_dotenv(dotenv_path=dotenv_path)
print(f"Loading .env from: {dotenv_path}")

# --- Configuration ---
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
if not LANGCHAIN_API_KEY:
    LANGCHAIN_API_KEY = str(uuid.uuid4())
    try:
        set_key(dotenv_path, "LANGCHAIN_API_KEY", LANGCHAIN_API_KEY, quote_mode="never")
        print(f"Generated new LANGCHAIN_API_KEY and saved to {dotenv_path}")
    except Exception as e:
        print(f"Error saving newly generated LANGCHAIN_API_KEY to .env: {e}. Key will be in-memory only.")
    print("Warning: LANGCHAIN_API_KEY was not set in .env. A new key has been generated.")
else:
    print("LANGCHAIN_API_KEY found in environment.")

CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./langchain_server/chroma_db_data")
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
VECTOR_DB_COLLECTION_PREFIX = os.getenv("VECTOR_DB_COLLECTION_PREFIX", "hrms_conv_")

# Warnings for missing critical API keys
if not GOOGLE_API_KEY or GOOGLE_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
    print("CRITICAL WARNING: GEMINI_API_KEY not found or is a placeholder. LLM functionality will be severely limited.")
# Add other ERPNext/Google Search key checks if necessary, they are used within tools now.

actual_chroma_path = CHROMA_DB_PATH
if not os.path.isabs(actual_chroma_path):
    actual_chroma_path = os.path.join(os.path.dirname(dotenv_path), actual_chroma_path)
    actual_chroma_path = os.path.normpath(actual_chroma_path)
os.makedirs(actual_chroma_path, exist_ok=True)
CHROMA_DB_PATH = actual_chroma_path
print(f"ChromaDB path set to: {CHROMA_DB_PATH}")


# --- Langchain & LLM Setup (Main LLM instance for agents) ---
llm = None
if GOOGLE_API_KEY and GOOGLE_API_KEY != "YOUR_GEMINI_API_KEY_HERE":
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=GOOGLE_API_KEY,
            convert_system_message_to_human=True
        )
        print("Google Generative AI (Gemini) model initialized for main server.")
    except Exception as e:
        print(f"Error initializing main Google Generative AI: {e}")
        llm = None
else:
    print("Error: GEMINI_API_KEY not found or is placeholder. LLM for agents is disabled.")

# --- Chroma DB Client ---
chroma_client = None
embedding_func = None
try:
    embedding_func = embedding_functions.DefaultEmbeddingFunction()
    chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    print(f"ChromaDB client initialized. Path: {CHROMA_DB_PATH}")
except Exception as e:
    print(f"Error initializing ChromaDB client: {e}")
    chroma_client = None

# --- Chat History Management ---
# This store will hold ChatMessageHistory objects for each session
chat_history_store = {}

def get_session_history(session_id: str) -> ChatMessageHistory:
    """Retrieves or creates chat history for a session, loading from ChromaDB if available."""
    if session_id not in chat_history_store:
        history_from_db = load_history_from_chromadb(session_id)
        chat_history_store[session_id] = history_from_db if history_from_db else ChatMessageHistory()
    return chat_history_store[session_id]

# --- Agent Executor with History (Using Routing Agent as the entry point) ---
# The routing_agent_executor is already an AgentExecutor. We need to wrap it with history.
agent_with_history = None
if routing_agent_executor: # Check if the routing agent was initialized successfully
    try:
        agent_with_history = RunnableWithMessageHistory(
            routing_agent_executor, # The routing agent is the primary interface
            get_session_history,
            input_messages_key="input",
            history_messages_key="history",
            # agent_scratchpad is handled within the create_tool_calling_agent used by routing_agent
        )
        print("Main agent (Routing Agent with history) wrapper initialized.")
    except Exception as e:
        print(f"Error initializing main agent with history: {e}")
else:
    print("Routing agent executor not available. Main agent with history cannot be initialized.")


# --- ChromaDB Helper Functions ---
def get_chroma_collection_name(session_id: str) -> str:
    return f"{VECTOR_DB_COLLECTION_PREFIX}{session_id.replace('-', '_')}"

def save_message_to_chromadb(session_id: str, sender: str, message: str, msg_type: str = "chat"):
    if not chroma_client or not embedding_func:
        print("ChromaDB client or embedding function not available. Skipping save.")
        return
    try:
        collection_name = get_chroma_collection_name(session_id)
        collection = chroma_client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_func
        )
        message_id = f"{session_id}_{uuid.uuid4()}"
        collection.add(
            documents=[message],
            metadatas=[{"sender": sender, "type": msg_type, "timestamp": str(uuid.uuid4())}], # Add timestamp for potential sorting
            ids=[message_id]
        )
        print(f"Stored '{sender}' message in ChromaDB collection '{collection_name}'.")
    except Exception as e:
        print(f"Error storing message in ChromaDB collection '{collection_name}': {e}")

def load_history_from_chromadb(session_id: str) -> ChatMessageHistory | None:
    if not chroma_client:
        print("ChromaDB client not available. Cannot load history.")
        return None
    try:
        collection_name = get_chroma_collection_name(session_id)
        # Check if collection exists before trying to get it
        # This check might vary depending on chromadb version; older versions might raise an error.
        # A robust way is to list collections and check. For simplicity, we'll try-except.
        try:
            collection = chroma_client.get_collection(name=collection_name, embedding_function=embedding_func)
        except Exception: # Catch specific exception if known, e.g. CollectionNotFoundError
            print(f"ChromaDB collection '{collection_name}' not found for session {session_id}.")
            return None


        results = collection.get(include=["metadatas", "documents"])
        if not results or not results.get("ids"):
            return None

        # Sort messages by timestamp if available, otherwise by ID (less reliable)
        # Ensure metadata and documents are not None before zipping
        ids = results.get("ids", [])
        docs = results.get("documents", [])
        metas = results.get("metadatas", [])

        if not (len(ids) == len(docs) == len(metas)):
            print(f"Warning: Mismatch in lengths of ids, documents, metadatas for session {session_id}. History might be incomplete.")
            # Potentially try to recover or return None / partial history
            return ChatMessageHistory() # Return empty history to avoid crashing

        combined = []
        for i in range(len(ids)):
            # Ensure each element exists before accessing
            doc_id = ids[i] if ids and i < len(ids) else None
            doc_content = docs[i] if docs and i < len(docs) else None
            meta_content = metas[i] if metas and i < len(metas) else {} # Default to empty dict for meta
            if doc_id and doc_content: # Only add if essential parts are present
                 combined.append((doc_id, doc_content, meta_content))


        # Sort by timestamp if present in metadata, otherwise fallback to ID (less reliable)
        try:
            combined.sort(key=lambda x: x[2].get("timestamp", x[0]))
        except Exception as sort_e:
            print(f"Could not sort history by timestamp for session {session_id}, falling back to ID sort: {sort_e}")
            combined.sort(key=lambda x: x[0])


        history = ChatMessageHistory()
        for _, doc, meta in combined:
            sender = meta.get("sender")
            if sender == "user":
                history.add_user_message(doc)
            elif sender == "ai":
                history.add_ai_message(doc)
            # Could add handling for 'agent_tool_log' if needed in history object

        print(f"Loaded {len(history.messages)} messages from ChromaDB for session {session_id}")
        return history
    except Exception as e:
        print(f"Could not load history from ChromaDB collection '{get_chroma_collection_name(session_id)}': {e}")
        return None

# --- FastAPI Setup ---
app = FastAPI(
    title="HRMS AI Agents - Langchain Server (Refactored)",
    version="0.4.0",
    description="Provides LLM chat, planning, and RAG capabilities using modular tools and agents."
)
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

# --- Security Dependency ---
async def verify_api_key(x_api_key: str = Depends(api_key_header)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="Missing X-API-Key header")
    if x_api_key != LANGCHAIN_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

# --- Pydantic Models ---
class TaskStep(BaseModel):
    step_number: int
    action: str
    details: str | dict

class LangchainResponse(BaseModel):
    session_id: str
    vector_db_ref: str | None = None
    response_type: str # "reply", "plan", "error"
    reply: str | None = None
    plan: list[TaskStep] | None = None
    error_message: str | None = None

class ChatMessageInput(BaseModel):
    message: str
    session_id: str | None = None

class ToolInput(BaseModel):
    tool_name: str
    arguments: dict # Arguments for the tool
    session_id: str | None = None # Optional, for tools that might interact with session history (though less common for direct tool calls)

class AgentInput(BaseModel):
    agent_name: str # "routing" or "data_retrieval"
    input_message: str
    session_id: str | None = None


# --- API Endpoints ---
@app.post("/chat", response_model=LangchainResponse, dependencies=[Depends(verify_api_key)])
async def handle_chat(payload: ChatMessageInput):
    if not llm or not agent_with_history: # agent_with_history uses routing_agent_executor
        detail_msg = "LLM Service or Main Agent (Routing Agent with History) not available."
        if not llm: detail_msg = "LLM Service not available (check GEMINI_API_KEY)."
        elif not agent_with_history: detail_msg = "Main Agent (Routing with History) not initialized."
        return LangchainResponse(
            session_id=payload.session_id or "unknown_session",
            response_type="error",
            error_message=detail_msg
        )

    session_id = payload.session_id or str(uuid.uuid4())
    user_message = payload.message
    vector_db_ref = get_chroma_collection_name(session_id)

    print(f"Received chat message for session {session_id}: {user_message}")
    save_message_to_chromadb(session_id, "user", user_message, msg_type="chat_request")

    agent_input = {"input": user_message}
    config = {"configurable": {"session_id": session_id}}

    try:
        # The routing_agent_executor (wrapped in agent_with_history) will handle planning and tool use.
        # Its direct output is considered the AI's response or a structured plan.
        agent_response_dict = await agent_with_history.ainvoke(agent_input, config=config)
        
        # The 'output' from the AgentExecutor is the final textual response from the LLM after agent execution.
        ai_final_response = agent_response_dict.get("output", "Agent did not produce a final output.")

        # The routing agent's prompt asks it to format plans. We check if the response looks like a plan.
        # This is a simplified check; more robust plan detection might be needed.
        parsed_plan: list[TaskStep] | None = None
        response_type = "reply" # Default

        # Heuristic to check if the response is a plan (e.g., starts with "1.")
        # A more robust method would be for the routing agent to use a specific tool or format for plans.
        if ai_final_response.strip().startswith("1."): # Basic check
            try:
                steps_raw = ai_final_response.split('\n')
                current_plan = []
                step_num = 1
                for line in steps_raw:
                    line_stripped = line.strip()
                    if line_stripped and (line_stripped[0].isdigit() and (line_stripped[1] == '.' or line_stripped[1] == ')')):
                        action_detail = line_stripped.split(maxsplit=1)[1] if len(line_stripped.split(maxsplit=1)) > 1 else line_stripped
                        # Action guess is harder now as the routing agent itself describes the action
                        current_plan.append(TaskStep(step_number=step_num, action="planned_step", details=action_detail))
                        step_num +=1
                if current_plan:
                    parsed_plan = current_plan
                    response_type = "plan"
            except Exception as e:
                print(f"Could not parse plan from agent output: {e}")
                # Fallback to reply if parsing fails

        save_message_to_chromadb(session_id, "ai", ai_final_response, msg_type=response_type)
        
        return LangchainResponse(
            reply=ai_final_response, # Return the full agent output
            plan=parsed_plan,
            session_id=session_id,
            vector_db_ref=vector_db_ref,
            response_type=response_type
        )

    except Exception as e:
        # Capture detailed traceback
        tb_str = traceback.format_exc()
        error_detail = f"Error invoking main agent for session {session_id}: {type(e).__name__} - {e}\nTraceback:\n{tb_str}"
        print(error_detail)
        status_code = 500
        if isinstance(e, HTTPException):
            error_detail = e.detail if hasattr(e, 'detail') else error_detail # Keep original detail for HTTPExceptions
            status_code = e.status_code
        
        save_message_to_chromadb(session_id, "ai_error", error_detail, msg_type="error")
        return LangchainResponse(
            session_id=session_id,
            vector_db_ref=vector_db_ref,
            response_type="error",
            error_message=error_detail
        )

# The /plan_task endpoint might become redundant if the /chat endpoint,
# via the routing_agent, can produce plans.
# For now, let's keep it but make it also use the routing_agent with a specific prompt for planning.
@app.post("/plan_task", response_model=LangchainResponse, dependencies=[Depends(verify_api_key)])
async def plan_task_endpoint(payload: ChatMessageInput):
    """
    Explicitly asks the Routing Agent to generate a plan for the given message.
    """
    if not llm or not agent_with_history: # agent_with_history uses routing_agent_executor
        detail_msg = "LLM Service or Main Agent not available for planning."
        # ... (add specific checks)
        return LangchainResponse(session_id=payload.session_id or "unknown_session", response_type="error", error_message=detail_msg)

    session_id = payload.session_id or str(uuid.uuid4())
    user_message = payload.message
    vector_db_ref = get_chroma_collection_name(session_id)

    print(f"Received explicit planning request for session {session_id}: {user_message}")
    save_message_to_chromadb(session_id, "user", user_message, msg_type="explicit_plan_request")

    # Instruct the routing agent to focus on planning
    planning_focused_input = (
        f"Please create a detailed, step-by-step plan to address the following user request. "
        f"Do not execute the steps yet. Focus on outlining the actions, tools to be used, and necessary inputs. "
        f"User Request: '{user_message}'"
    )
    
    agent_input = {"input": planning_focused_input}
    config = {"configurable": {"session_id": session_id}}

    try:
        agent_response_dict = await agent_with_history.ainvoke(agent_input, config=config)
        ai_plan_description = agent_response_dict.get("output", "Agent did not produce a plan description.")

        parsed_plan: list[TaskStep] | None = None
        try:
            steps_raw = ai_plan_description.split('\n')
            current_plan = []
            step_num = 1
            for line in steps_raw:
                line_stripped = line.strip()
                if line_stripped and (line_stripped[0].isdigit() and (line_stripped[1] == '.' or line_stripped[1] == ')')):
                    action_detail = line_stripped.split(maxsplit=1)[1] if len(line_stripped.split(maxsplit=1)) > 1 else line_stripped
                    current_plan.append(TaskStep(step_number=step_num, action="planned_step", details=action_detail))
                    step_num +=1
            if current_plan:
                parsed_plan = current_plan
        except Exception as e:
            print(f"Could not parse plan from explicit planning output: {e}")
            # ai_plan_description will be returned as 'reply'

        save_message_to_chromadb(session_id, "ai", ai_plan_description, msg_type="plan_generated")

        return LangchainResponse(
            reply=ai_plan_description, # The textual description of the plan
            plan=parsed_plan,          # The parsed plan structure
            session_id=session_id,
            vector_db_ref=vector_db_ref,
            response_type="plan" if parsed_plan else "reply" # Mark as plan if parsing succeeded
        )
    except Exception as e:
        # Capture detailed traceback
        tb_str = traceback.format_exc()
        error_detail = f"Error invoking agent for explicit planning (session {session_id}): {type(e).__name__} - {e}\nTraceback:\n{tb_str}"
        print(error_detail)
        status_code = 500
        if isinstance(e, HTTPException):
            error_detail = e.detail if hasattr(e, 'detail') else error_detail # Keep original detail for HTTPExceptions
            status_code = e.status_code
        save_message_to_chromadb(session_id, "ai_error", error_detail, msg_type="error")
        return LangchainResponse(session_id=session_id, vector_db_ref=vector_db_ref, response_type="error", error_message=error_detail)


@app.post("/invoke_tool", dependencies=[Depends(verify_api_key)])
async def invoke_tool_endpoint(payload: ToolInput):
    """
    Directly invokes a specified tool with given arguments.
    """
    tool_to_invoke = available_tools_map.get(payload.tool_name)
    if not tool_to_invoke:
        raise HTTPException(status_code=404, detail=f"Tool '{payload.tool_name}' not found.")

    print(f"Directly invoking tool: {payload.tool_name} with args: {payload.arguments}")
    
    try:
        # Check if the tool supports asynchronous invocation (has an arun method)
        if hasattr(tool_to_invoke, 'arun'):
            tool_result = await tool_to_invoke.arun(payload.arguments)
        else:
            # For synchronous tools, run them in a thread pool to avoid blocking asyncio event loop
            tool_result = await asyncio.to_thread(tool_to_invoke.run, payload.arguments)
        
        # If session_id is provided, one might log this tool invocation, but it's optional for direct calls
        if payload.session_id:
            log_message = f"Direct tool invocation: {payload.tool_name}, Args: {json.dumps(payload.arguments)}, Result: {str(tool_result)[:200]}..."
            save_message_to_chromadb(payload.session_id, "system_tool_direct_call", log_message, msg_type="direct_tool_log")

        return {"tool_name": payload.tool_name, "arguments": payload.arguments, "result": tool_result}
    except Exception as e:
        # Capture detailed traceback
        tb_str = traceback.format_exc()
        error_detail = f"Error invoking tool {payload.tool_name}: {type(e).__name__} - {e}\nTraceback:\n{tb_str}"
        print(error_detail)
        # If session_id is provided, log the error
        if payload.session_id:
             save_message_to_chromadb(payload.session_id, "system_tool_direct_call_error", error_detail, msg_type="direct_tool_error")
        # For direct tool invocation, re-raise as HTTPException to return error to client
        raise HTTPException(status_code=500, detail=error_detail)


@app.post("/invoke_agent", response_model=LangchainResponse, dependencies=[Depends(verify_api_key)])
async def invoke_agent_endpoint(payload: AgentInput):
    """
    Directly invokes a specified agent with a given input message and optional session_id for history.
    """
    session_id = payload.session_id or str(uuid.uuid4()) # Ensure session_id for history
    vector_db_ref = get_chroma_collection_name(session_id)
    
    agent_executor_to_invoke = None
    agent_name_for_log = ""

    if payload.agent_name.lower() == "routing":
        agent_executor_to_invoke = routing_agent_executor
        agent_name_for_log = "RoutingAgent"
    elif payload.agent_name.lower() == "data_retrieval":
        agent_executor_to_invoke = data_retrieval_agent_executor
        agent_name_for_log = "DataRetrievalAgent"
    else:
        return LangchainResponse(
            session_id=session_id,
            vector_db_ref=vector_db_ref,
            response_type="error",
            error_message=f"Agent '{payload.agent_name}' not found. Available agents: 'routing', 'data_retrieval'."
        )

    if not agent_executor_to_invoke:
        return LangchainResponse(
            session_id=session_id,
            vector_db_ref=vector_db_ref,
            response_type="error",
            error_message=f"{agent_name_for_log} is not initialized (LLM or configuration issue)."
        )

    print(f"Directly invoking {agent_name_for_log} for session {session_id} with input: {payload.input_message}")
    save_message_to_chromadb(session_id, "user_direct_agent_invoke", f"Invoking {agent_name_for_log}: {payload.input_message}", msg_type="direct_agent_request")

    # Prepare agent input and config for history
    agent_call_input = {"input": payload.input_message}
    config = {"configurable": {"session_id": session_id}}
    
    # Wrap the chosen agent_executor with history for this call
    # This is crucial because the agent executors themselves are not history-aware by default
    current_agent_with_history = RunnableWithMessageHistory(
        agent_executor_to_invoke,
        get_session_history, # Uses the shared history store and ChromaDB functions
        input_messages_key="input",
        history_messages_key="history",
    )

    try:
        agent_response_dict = await current_agent_with_history.ainvoke(agent_call_input, config=config)
        ai_final_response = agent_response_dict.get("output", f"{agent_name_for_log} did not produce a final output.")
        
        # For direct agent calls, the output is typically a "reply"
        # Plan parsing logic similar to /chat could be added if agents are expected to return plans here
        response_type = "reply"
        parsed_plan = None # Placeholder for potential plan parsing

        save_message_to_chromadb(session_id, "ai_direct_agent_response", ai_final_response, msg_type=response_type)

        return LangchainResponse(
            reply=ai_final_response,
            plan=parsed_plan,
            session_id=session_id,
            vector_db_ref=vector_db_ref,
            response_type=response_type
        )
    except Exception as e:
        # Capture detailed traceback
        tb_str = traceback.format_exc()
        error_detail = f"Error invoking {agent_name_for_log} (session {session_id}): {type(e).__name__} - {e}\nTraceback:\n{tb_str}"
        print(error_detail)
        status_code = 500
        if isinstance(e, HTTPException):
            error_detail = e.detail if hasattr(e, 'detail') else error_detail # Keep original detail for HTTPExceptions
            status_code = e.status_code
        save_message_to_chromadb(session_id, "ai_direct_agent_error", error_detail, msg_type="error")
        return LangchainResponse(session_id=session_id, vector_db_ref=vector_db_ref, response_type="error", error_message=error_detail)


@app.get("/health")
async def health_check():
    llm_status = "initialized" if llm else "not_initialized"
    chroma_status = "connected" if chroma_client else "disconnected"
    routing_agent_status = "initialized" if routing_agent_executor else "not_initialized"
    data_agent_status = "initialized" if data_retrieval_agent_executor else "not_initialized"
    main_agent_history_status = "initialized" if agent_with_history else "not_initialized"
    return {
        "status": "ok",
        "llm_status": llm_status,
        "chroma_client_status": chroma_status,
        "routing_agent_status": routing_agent_status,
        "data_retrieval_agent_status": data_agent_status,
        "main_agent_with_history_status": main_agent_history_status
    }

if __name__ == "__main__":
    import uvicorn
    import asyncio # Required for running async tools if invoked directly in __main__ for testing
    import traceback # Import traceback module

    print(f"Starting Langchain Server (Refactored with Direct Invocation Endpoints)...")
    print(f"API Key Auth: {'Enabled' if LANGCHAIN_API_KEY else 'Disabled (Warning!)'}")
    print(f"Chroma DB Path: {CHROMA_DB_PATH}")
    if not GOOGLE_API_KEY or GOOGLE_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        print("CRITICAL ERROR: GEMINI_API_KEY not found or is placeholder. LLM will not function.")
    uvicorn.run(app, host="0.0.0.0", port=8500, log_level="info")