from .state import AgentState
from langchain_core.messages import ToolMessage
from langchain_groq import ChatGroq
from langgraph.prebuilt import ToolNode
from ..memory.vector_store import save_summary_to_memory, retrieve_from_memory
from dotenv import load_dotenv
from ..tools.arxiv_search import arxivsearch
from ..tools.google_search import googlesearch
from ..tools.pdf_reader import pdfreader



all_tools = [arxivsearch, googlesearch, pdfreader,save_summary_to_memory,retrieve_from_memory]

load_dotenv()

llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct").bind_tools(all_tools)

def planner_node(state: AgentState):
    """
    This is the "brain" of the agent.
    It calls the LLM with the current state to decide what to do next.
    """
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools=all_tools)