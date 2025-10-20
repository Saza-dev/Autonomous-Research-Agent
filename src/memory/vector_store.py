import chromadb
import uuid
from langchain_core.tools import tool
from typing import List, Union


client = chromadb.PersistentClient(path="./chromadb_store")
collection = client.get_or_create_collection(name="research_summaries")

@tool
def save_summary_to_memory(summary_text: str) -> str:
    """
    Saves a given text summary into the vector memory.
    Use this after reading a paper or article to remember its key findings.
    """
    if collection is None:
        return "Error: Memory collection is not initialized."
        
    try:
        # We need a unique ID for each document
        doc_id = str(uuid.uuid4())
        
        collection.add(
            documents=[summary_text],
            ids=[doc_id]
        )
        return "Successfully saved summary to memory."
        
    except Exception as e:
        return f"Error: Failed to save summary to memory: {str(e)}"


@tool
def retrieve_from_memory(query: str, n_results: int = 3) -> Union[str, List[str]]:
    """
    Retrieves relevant information from the vector memory based on a query.
    Use this at the *start* of your research to see what you already know.
    """
    if collection is None:
        return "Error: Memory collection is not initialized."
        
    try:
        results = collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        retrieved_docs = results.get('documents', [[]])[0]
        
        if not retrieved_docs:
            return "No relevant information found in memory for that query."
        return retrieved_docs
        
    except Exception as e:
        return f"Error: Failed to retrieve from memory: {str(e)}"
