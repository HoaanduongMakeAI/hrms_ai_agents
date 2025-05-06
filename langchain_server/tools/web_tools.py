import os
import json
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from googleapiclient.discovery import build as google_build
import asyncio # Import asyncio for async operations
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError, Browser, Playwright # Import necessary Playwright types
from langchain_core.tools import tool
from dotenv import load_dotenv

# Load from the .env file located two levels up (in the app root)
# This assumes web_tools.py is in langchain_server/tools/
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

# Google Custom Search Configuration
GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

# --- Playwright Global Instance ---
playwright_instance: Playwright | None = None
browser_instance: Browser | None = None

async def initialize_playwright():
    """Initializes the Playwright browser instance."""
    global playwright_instance, browser_instance
    if browser_instance is None:
        print("Initializing Playwright browser...")
        try:
            playwright_instance = await async_playwright().start()
            browser_instance = await playwright_instance.chromium.launch()
            print("Playwright browser initialized successfully.")
        except Exception as e:
            print(f"Error initializing Playwright browser: {e}")
            playwright_instance = None
            browser_instance = None

async def close_playwright():
    """Closes the Playwright browser instance."""
    global playwright_instance, browser_instance
    if browser_instance:
        print("Closing Playwright browser...")
        await browser_instance.close()
        browser_instance = None
        print("Playwright browser closed.")
    if playwright_instance:
        await playwright_instance.stop()
        playwright_instance = None
        print("Playwright instance stopped.")


# --- Google Custom Search Tool ---
@tool
def google_custom_search(query: str, num_results: int = 5) -> dict:
    """
    Performs a Google Custom Search for the given query and returns top URLs.
    Input:
        query (string): The search query.
        num_results (int): Number of search results to return (default 5, max 10).
    Output:
        A dictionary containing a list of 'urls' or an 'error' message.
    """
    if not GOOGLE_SEARCH_API_KEY or GOOGLE_SEARCH_API_KEY == "YOUR_GOOGLE_SEARCH_API_KEY" or \
       not GOOGLE_CSE_ID or GOOGLE_CSE_ID == "YOUR_GOOGLE_CSE_ID":
        return {"error": "Google Custom Search API key or CSE ID not configured or are placeholders."}
    try:
        service = google_build("customsearch", "v1", developerKey=GOOGLE_SEARCH_API_KEY)
        result = service.cse().list(q=query, cx=GOOGLE_CSE_ID, num=min(num_results, 10)).execute()
        urls = [item['link'] for item in result.get('items', [])]
        return {"urls": urls}
    except Exception as e:
        print(f"Error during Google Custom Search: {e}")
        return {"error": f"Google Custom Search failed: {str(e)}"}

# --- Playwright Scraping Helper ---
async def _scrape_with_playwright(url: str) -> str:
    """Helper for Playwright scraping using the global browser instance."""
    if browser_instance is None:
        return "Error: Playwright browser not initialized."

    try:
        # Use the existing browser instance to create a new page
        page = await browser_instance.new_page()
        await page.goto(url, timeout=20000) # Increased timeout
        html_content = await page.content()
        await page.close() # Close the page, but keep the browser open
        return html_content
    except PlaywrightTimeoutError:
        return f"Playwright timed out trying to load URL: {url}. The page might be too slow or require complex interactions not handled."
    except Exception as e:
        return f"Error scraping with Playwright for URL {url}: {str(e)}"

# --- Scrape Website Tool ---
@tool
async def scrape_website_to_markdown(url: str, use_playwright: bool = False) -> str:
    """
    Fetches content from a URL and converts its main HTML content to Markdown.
    Uses BeautifulSoup by default. If use_playwright is True, it uses Playwright
    for dynamic content.
    Input:
        url (string): The URL to scrape.
        use_playwright (bool): Set to True to use Playwright for dynamic pages. Default is False.
    Output:
        Markdown content as a string, or an error message.
    """
    html_content = ""
    try:
        print(f"Scraping URL: {url} (Playwright: {use_playwright})")
        if use_playwright:
            # Ensure Playwright is initialized before using it
            await initialize_playwright()
            html_content = await _scrape_with_playwright(url)
            if html_content.startswith("Error scraping with Playwright") or html_content.startswith("Playwright timed out"):
                 return html_content
        else:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = requests.get(url, timeout=15, headers=headers)
            response.raise_for_status()
            html_content = response.text

        if not html_content:
            return "Error: No HTML content fetched."

        soup = BeautifulSoup(html_content, 'html.parser')
        
        main_content = soup.find('article') or \
                       soup.find('main') or \
                       soup.find('div', role='main') or \
                       soup.find('div', class_=lambda x: x and 'content' in x.lower()) or \
                       soup.find('div', id=lambda x: x and 'content' in x.lower())

        if main_content:
            markdown_text = md(str(main_content), heading_style="ATX")
        else:
            markdown_text = md(str(soup.body), heading_style="ATX")
            
        return markdown_text[:15000] # Limit content length
    except requests.exceptions.Timeout:
        return f"Error: Request timed out for URL {url} using requests."
    except requests.exceptions.HTTPError as e:
        return f"Error: HTTP {e.response.status_code} for URL {url} using requests."
    except requests.exceptions.RequestException as e:
        return f"Error fetching URL {url} with requests: {e}"
    except Exception as e:
        return f"Error processing URL {url}: {str(e)}"

# List of web tools to be imported by the main agent setup
web_tools_list = [
    google_custom_search,
    scrape_website_to_markdown,
]

# Note: Playwright initialization and closing will be managed by the FastAPI application's
# startup and shutdown events in main.py to ensure it runs within the correct event loop.
# The initialize_playwright and close_playwright functions are kept here to be called by main.py.