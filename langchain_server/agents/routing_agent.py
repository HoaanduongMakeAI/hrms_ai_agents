from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Import tools from their respective modules using absolute paths relative to langchain_server
from tools.erpnext_tools import erpnext_tools_list
from tools.web_tools import web_tools_list

# Combine all available tools
all_tools = erpnext_tools_list + web_tools_list

# Load Gemini API Key
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
llm = None
if GOOGLE_API_KEY:
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", 
        google_api_key=GOOGLE_API_KEY,
        convert_system_message_to_human=True
    )
else:
    print("WARNING: GEMINI_API_KEY not found. Routing agent will not function properly.")

# Define the prompt template for the Routing & Planning Agent
# This prompt needs to guide the LLM on how to understand user requests,
# identify intents, extract entities, and plan steps, possibly by selecting other specialized agents or tools.
ROUTING_AGENT_SYSTEM_PROMPT = """
You are a highly intelligent Routing and Planning Agent. Your primary responsibilities are:
1.  **Understand User Request**: Deeply analyze the user's message to grasp their intent and any specific entities mentioned (e.g., DocType names, document IDs, search queries, URLs).
2.  **Identify Intent**: Determine the primary goal of the user's request. Is it to retrieve information, create data, update data, delete data, search the web, scrape a webpage, or a more complex multi-step task?
3.  **Extract Entities**: Identify key pieces of information from the user's request that are necessary for fulfilling it.
4.  **Plan Execution Steps**: Based on the intent and entities, formulate a clear, step-by-step plan. This plan might involve:
    *   Directly using one or more available tools.
    *   Delegating the task to a more specialized agent (if other agents are defined and available).
    *   Asking the user for clarification if the request is ambiguous or information is missing.
5.  **Tool Selection**: If a direct tool use is part of the plan, clearly state which tool should be used and what the input for that tool should be.

**Available Tools for Planning (you can suggest using these in your plan):**
{tool_descriptions}

**Output Format for Planning:**
If the request requires planning, provide the plan as a numbered list. Each step should clearly state the action.
If the request is simple and can be handled by a direct tool call you are equipped with, you can also execute that.
If the request requires another specialized agent, state which agent should be called and what information should be passed to it.

**Example Plan Output:**
1. Tool: `erpnext_get_doctype_structure`, Input: `doctype_name="Employee"` (To understand employee data structure).
2. Ask user for the following details for the new employee: [list missing fields based on structure].
3. Tool: `erpnext_create_document`, Input: `doctype_name="Employee"`, `data={{employee_data_from_user}}`.

**Clarification:**
If the user's request is unclear or lacks necessary information (e.g., "update the record" without specifying which record), ALWAYS ask for clarification before proceeding with a plan or action. Example: "Could you please specify the DocType and Document ID of the record you'd like to update?"

Your goal is to create a logical and efficient plan to address the user's needs.
You have access to a set of tools. You are responsible for deciding which tool(s) to use and in what order.
"""

def get_tool_descriptions(tools):
    return "\n".join([f"- `{tool.name}`: {tool.description}" for tool in tools])

routing_agent_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", ROUTING_AGENT_SYSTEM_PROMPT.format(tool_descriptions=get_tool_descriptions(all_tools))),
        MessagesPlaceholder(variable_name="history"), # For chat history context
        ("human", "{input}"), # User's current message
        MessagesPlaceholder(variable_name="agent_scratchpad"), # For agent's intermediate steps & tool outputs
    ]
)

# Create the Routing Agent
routing_agent = None
routing_agent_executor = None

if llm:
    try:
        routing_agent_runnable = create_tool_calling_agent(llm, all_tools, routing_agent_prompt)
        routing_agent_executor = AgentExecutor(
            agent=routing_agent_runnable,
            tools=all_tools,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=10,
        )
        print("Routing & Planning Agent initialized.")
    except Exception as e:
        print(f"Error initializing Routing & Planning Agent: {e}")
else:
    print("LLM not available, Routing & Planning Agent not initialized.")

# Example of how this agent might be invoked (this would typically be part of the main server logic)
# async def invoke_routing_agent(user_input: str, session_history):
#     if not routing_agent_executor:
#         return {"error": "Routing agent not initialized."}
#     
#     response = await routing_agent_executor.ainvoke({
#         "input": user_input,
#         "history": session_history.messages # Assuming session_history is a ChatMessageHistory object
#     })
#     return response