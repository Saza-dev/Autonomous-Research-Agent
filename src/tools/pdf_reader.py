import requests, fitz
from io import BytesIO
from langchain_core.tools import tool

@tool
def pdf_reader(url):
    """
    Downloads a PDF from the given URL and extracts all text.
    Returns the extracted text, or a clear error message if it fails.
    """

    try:
        response = requests.get(url)

        pdf_bytes = BytesIO(response.content)
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        text = ""
        for page in doc:
            text += page.get_text("text")
        doc.close()

        return(text)
    
    except requests.exceptions.HTTPError as e:
        return f"Error: Failed to download file. HTTP Status Code: {e.response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: Failed to download file. Network error: {str(e)}"
    except fitz.errors.EmptyFileError:
        return "Error: The downloaded file is empty or a corrupted PDF."
    except Exception as e:
        return f"Error: An unexpected error occurred: {str(e)}"
