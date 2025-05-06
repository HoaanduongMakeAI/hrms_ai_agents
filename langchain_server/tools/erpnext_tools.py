import os
import json
import requests
from fastapi import HTTPException # Assuming this server runs with FastAPI
from langchain_core.tools import tool
from dotenv import load_dotenv

# Load from the .env file located two levels up (in the app root)
# This assumes erpnext_tools.py is in langchain_server/tools/
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

# ERPNext Configuration - these should be loaded from .env
ERPNext_API_URL = os.getenv("ERPNext_API_URL")
ERPNext_API_KEY = os.getenv("ERPNext_API_KEY")
ERPNext_API_SECRET = os.getenv("ERPNext_API_SECRET")

def make_erpnext_request(method: str, endpoint: str, data: dict = None, params: dict = None) -> dict:
    """Helper function to make authenticated requests to ERPNext API."""
    if not ERPNext_API_URL or not ERPNext_API_KEY or not ERPNext_API_SECRET or \
       ERPNext_API_KEY == "YOUR_ERPNext_API_KEY" or ERPNext_API_SECRET == "YOUR_ERPNext_API_SECRET": # Check for placeholder values
        raise HTTPException(status_code=500, detail="ERPNext API credentials not configured or are placeholders.")

    headers = {
        "Authorization": f"token {ERPNext_API_KEY}:{ERPNext_API_SECRET}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    if not endpoint.startswith('/api'):
        if endpoint.startswith('/'):
            url = f"{ERPNext_API_URL}/api{endpoint}"
        else:
            url = f"{ERPNext_API_URL}/api/{endpoint}"
    else:
        url = f"{ERPNext_API_URL}{endpoint}"

    try:
        print(f"Making ERPNext request: {method.upper()} {url}")
        if data:
            print(f"Request data: {json.dumps(data)[:200]}...")
        if params:
            print(f"Request params: {params}")

        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=30)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=data, params=params, timeout=30)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, json=data, params=params, timeout=30)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers, params=params, timeout=30)
        else:
            raise HTTPException(status_code=500, detail=f"Unsupported HTTP method: {method}")

        response.raise_for_status()
        
        if response.status_code == 204:
            return {"status": "success", "message": "Operation successful, no content returned."}
        if not response.content:
             return {"status": "success", "message": "Operation successful, no JSON content returned."}

        return response.json()
    except requests.exceptions.HTTPError as e:
        error_message = f"HTTPError calling ERPNext: {e.response.status_code}"
        try:
            erp_error = e.response.json()
            if "_server_messages" in erp_error:
                server_messages = json.loads(erp_error["_server_messages"])
                messages = [msg.get("message", str(msg)) for msg in server_messages]
                error_message += f" - Server Messages: {'; '.join(messages)}"
            elif "exception" in erp_error:
                 error_message += f" - Exception: {erp_error['exception']}"
            elif "error" in erp_error:
                error_message += f" - Error: {erp_error['error']}"
            else:
                error_message += f" - Raw Response: {e.response.text[:500]}"
        except ValueError:
             error_message += f" - Raw Response: {e.response.text[:500]}"
        print(error_message)
        raise HTTPException(status_code=e.response.status_code, detail=error_message)
    except requests.exceptions.RequestException as e:
        print(f"RequestException calling ERPNext: {e}")
        raise HTTPException(status_code=503, detail=f"ERPNext API connection error: {e}")
    except Exception as e:
        print(f"Unexpected error in make_erpnext_request: {e}")
        raise HTTPException(status_code=500, detail=f"Unexpected error during ERPNext API call: {str(e)}")

@tool
def erpnext_get_doctype_structure(doctype_name: str) -> dict:
    """
    Fetches the structure (meta) of a given DocType from ERPNext.
    Input: doctype_name (string) - The name of the DocType (e.g., "Employee", "Leave Application").
    """
    try:
        response = make_erpnext_request("GET", f"/api/method/frappe.desk.form.load.getdoctype", params={"doctype": doctype_name})
        if response and isinstance(response.get("docs"), list) and len(response["docs"]) > 0:
            doc_meta = response["docs"][0]
            return {
                "name": doc_meta.get("name"),
                "fields": [{"fieldname": f.get("fieldname"), "label": f.get("label"), "fieldtype": f.get("fieldtype"), "options": f.get("options"), "reqd": f.get("reqd")} for f in doc_meta.get("fields", [])],
                "permissions": doc_meta.get("permissions")
            }
        return response
    except HTTPException as e:
        return {"error": str(e.detail), "status_code": e.status_code}
    except Exception as e:
        return {"error": f"Unexpected error fetching DocType structure for {doctype_name}: {str(e)}"}

@tool
def erpnext_get_document(doctype_name: str, document_name: str, fields: list[str] = None) -> dict:
    """
    Fetches a specific document (entity) from ERPNext.
    Optionally specify a list of fields to retrieve.
    Input:
        doctype_name (string) - The name of the DocType (e.g., "Employee").
        document_name (string) - The unique name/ID of the document (e.g., "EMP-00001").
        fields (list[string], optional) - List of fields to fetch. e.g., ["employee_name", "status", "department"]
    """
    try:
        endpoint = f"/api/resource/{doctype_name}/{document_name}"
        params = {}
        if fields:
            params["fields"] = json.dumps(fields)

        response = make_erpnext_request("GET", endpoint, params=params)
        return response.get("data", response)
    except HTTPException as e:
        return {"error": str(e.detail), "status_code": e.status_code}
    except Exception as e:
        return {"error": f"Unexpected error fetching document {doctype_name}/{document_name}: {str(e)}"}

@tool
def erpnext_create_document(doctype_name: str, data: dict) -> dict:
    """
    Creates a new document (entity) in ERPNext.
    Input:
        doctype_name (string) - The name of the DocType (e.g., "Employee").
        data (dict) - A dictionary containing the field data for the new document.
                      Ensure this matches the DocType's structure.
    """
    try:
        response = make_erpnext_request("POST", f"/api/resource/{doctype_name}", data=data)
        return response.get("data", response)
    except HTTPException as e:
        return {"error": str(e.detail), "status_code": e.status_code}
    except Exception as e:
        return {"error": f"Unexpected error creating document in {doctype_name}: {str(e)}"}

@tool
def erpnext_update_document(doctype_name: str, document_name: str, data: dict) -> dict:
    """
    Updates an existing document (entity) in ERPNext.
    Input:
        doctype_name (string) - The name of the DocType (e.g., "Employee").
        document_name (string) - The unique name/ID of the document to update.
        data (dict) - A dictionary containing the fields to update and their new values.
    """
    try:
        response = make_erpnext_request("PUT", f"/api/resource/{doctype_name}/{document_name}", data=data)
        return response.get("data", response)
    except HTTPException as e:
        return {"error": str(e.detail), "status_code": e.status_code}
    except Exception as e:
        return {"error": f"Unexpected error updating document {doctype_name}/{document_name}: {str(e)}"}

@tool
def erpnext_delete_document(doctype_name: str, document_name: str) -> dict:
    """
    Deletes a document (entity) from ERPNext.
    Input:
        doctype_name (string) - The name of the DocType (e.g., "Leave Application").
        document_name (string) - The unique name/ID of the document to delete.
    """
    try:
        response = make_erpnext_request("DELETE", f"/api/resource/{doctype_name}/{document_name}")
        return response
    except HTTPException as e:
        return {"error": str(e.detail), "status_code": e.status_code}
    except Exception as e:
        return {"error": f"Unexpected error deleting document {doctype_name}/{document_name}: {str(e)}"}

@tool
def erpnext_execute_method(method_path: str, arguments: dict = None) -> dict:
    """
    Executes a whitelisted server-side Python method in ERPNext.
    Input:
        method_path (string): The full dotted Python path to the whitelisted method.
                              e.g., "my_app.my_module.utils.my_custom_function"
        arguments (dict, optional): Arguments to pass to the method.
                                    e.g. {"employee_id": "EMP-0001", "reason": "Test"}
    """
    try:
        response = make_erpnext_request("POST", f"/api/method/{method_path}", data=arguments or {})
        return response.get("message", response)
    except HTTPException as e:
        return {"error": str(e.detail), "status_code": e.status_code}
    except Exception as e:
        return {"error": f"Unexpected error executing method {method_path}: {str(e)}"}

# List of ERPNext tools to be imported by the main agent setup
erpnext_tools_list = [
    erpnext_get_doctype_structure,
    erpnext_get_document,
    erpnext_create_document,
    erpnext_update_document,
    erpnext_delete_document,
    erpnext_execute_method,
]