import arxiv
from langchain_core.tools import tool

@tool
def arxivsearch(query: str, max_results: int = 5) -> list:
    """
    Searches arXiv for a given query and returns a list of results
    with title, authors, summary, and PDF URL.
    Returns an error message string if the search fails.
    """
    try:
        client = arxiv.Client()
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )

        results = []

        for result in client.results(search):
            results.append({
                "title" : result.title,
                "authors" : [author.name for author in result.authors],
                "summary" : result.summary,
                "pdf_url":result.pdf_url
            })

        return results
    
    except arxiv.errors.BadQuery as e:
        return f"Error: Invalid arXiv query. The API reported: {str(e)}"
    except arxiv.errors.RequestException as e:
        return f"Error: Failed to connect to arXiv API. {str(e)}"
    except Exception as e:
        return f"Error: An unexpected error occurred during arXiv search: {str(e)}"
    
