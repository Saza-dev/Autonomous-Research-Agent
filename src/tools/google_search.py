from ddgs import DDGS
from langchain_core.tools import tool

@tool
def googlesearch(keywords: str, num_results: int = 2) -> list:
    """
    Performs a web search using DuckDuckGo and returns a list of results.
    Each result is a dictionary with 'title', 'url', and 'snippet'.
    Returns an error message string if the search fails.
    """
    output = []

    try:
        with DDGS() as ddgs:
            results = ddgs.text(keywords, max_results=num_results)
        for r in results:
                output.append({
                    "title": r.get('title', 'No Title Available'),
                    "url": r.get('href', 'No URL Available'),
                    "snippet": r.get('body', 'No Snippet Available')
                })
    except Exception as e:
        return (f"Search failed: {e}")

    return(output)