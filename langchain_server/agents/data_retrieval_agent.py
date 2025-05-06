import json
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Import tools from their respective modules using absolute paths relative to langchain_server
from tools.erpnext_tools import erpnext_get_document, erpnext_get_doctype_structure, erpnext_tools_list
from tools.web_tools import google_custom_search, scrape_website_to_markdown, web_tools_list

# Combine relevant tools for this agent
# This agent primarily uses tools for fetching data, not creating/modifying it.
data_retrieval_tools = [
    erpnext_get_document,
    erpnext_get_doctype_structure,
    google_custom_search,
    scrape_website_to_markdown,
]

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
    print("WARNING: GEMINI_API_KEY not found. Data Retrieval agent will not function properly.")

DATA_RETRIEVAL_AGENT_SYSTEM_PROMPT = """
You are a specialized Data Retrieval Agent. Your purpose is to fetch and process data from internal ERPNext systems and the external internet based on specific instructions.

**Core Functions:**
1.  **Internal Data Retrieval (ERPNext):**
    *   Fetch specific documents using `erpnext_get_document`. (Input: doctype_name, document_name, optional fields list)
    *   Fetch the structure of a DocType using `erpnext_get_doctype_structure`. (Input: doctype_name)
    *   Output for internal data should be in JSON format. If the tool returns JSON, pass it through. If it returns other structures, try to represent the key information as JSON.

2.  **Internet Data Retrieval:**
    *   Use `google_custom_search` to find relevant URLs for a query. (Input: query, num_results)
    *   Use `scrape_website_to_markdown` to get content from a specific URL. (Input: url, use_playwright for dynamic sites)
    *   Output for internet articles should be in Markdown format. The `scrape_website_to_markdown` tool already does this.

**Process Flow:**
*   You will be given a task, which might include a specific order of operations or target data points.
*   If the task involves multiple sources (e.g., "Get employee details for EMP-001 and find recent news about their department's industry"), process them sequentially as instructed or logically.
*   If specific URLs are provided for scraping, use them directly with `scrape_website_to_markdown`.
*   If search terms are provided, use `google_custom_search` first, then potentially `scrape_website_to_markdown` on the results if content extraction is needed.

**Output Requirements:**
*   For ERPNext data: Return data in JSON format.
*   For internet articles/web content: Return data in Markdown format.
*   If a task involves multiple data points, structure your final response clearly, perhaps using a dictionary with keys for each piece of retrieved data. For example:
    ```json
    {{
        "erpnext_employee_data": {{ ...employee json... }},
        "industry_article_markdown": "## Article Title\n...article content..."
    }}
    ```
*   If a tool fails, report the error clearly.

**Clarification:**
If the request is ambiguous (e.g., "get data about sales") or lacks specifics (e.g., which document, what search query), you should state what information is missing. However, your primary role is data retrieval based on provided inputs, so assume inputs are mostly specific. The Routing Agent is usually responsible for initial clarification.

You have access to the following tools:
{tool_descriptions}

Focus on retrieving and formatting the data as requested.
"""

def get_tool_descriptions(tools):
    return "\n".join([f"- `{tool.name}`: {tool.description}" for tool in tools])

data_retrieval_agent_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", DATA_RETRIEVAL_AGENT_SYSTEM_PROMPT.format(tool_descriptions=get_tool_descriptions(data_retrieval_tools))),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"), # This input should be a structured task from the Routing Agent or a direct request
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

data_retrieval_agent_executor = None
if llm:
    try:
        data_retrieval_agent_runnable = create_tool_calling_agent(llm, data_retrieval_tools, data_retrieval_agent_prompt)
        data_retrieval_agent_executor = AgentExecutor(
            agent=data_retrieval_agent_runnable,
            tools=data_retrieval_tools,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=8, # Data retrieval might involve a few steps (search then scrape)
        )
        print("Data Retrieval Agent initialized.")
    except Exception as e:
        print(f"Error initializing Data Retrieval Agent: {e}")
else:
    print("LLM not available, Data Retrieval Agent not initialized.")

# Example of how this agent might be invoked:
# async def invoke_data_retrieval_agent(task_details: dict, session_history):
#     if not data_retrieval_agent_executor:
#         return {"error": "Data Retrieval agent not initialized."}
#
#     # The 'input' for this agent is expected to be a clear instruction set
#     # e.g., "Fetch Employee/EMP-001 and scrape URL 'http://example.com/news'."
#     # This might come from the routing_agent's plan.
#     response = await data_retrieval_agent_executor.ainvoke({
#         "input": task_details.get("instruction", "No instruction provided."), 
#         "history": session_history.messages
#     })
#     return response