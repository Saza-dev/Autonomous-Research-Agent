from .state import AgentState
from langchain_core.messages import ToolMessage
from langchain_groq import ChatGroq
from langgraph.prebuilt import ToolNode
from langchain_core.tools import Tool
from dotenv import load_dotenv

from ..tools.arxiv_search import arxivsearch
from ..tools.google_search import googlesearch
from ..tools.pdf_reader import pdfreader



all_tools = [arxivsearch, googlesearch, pdfreader]

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile").bind_tools(all_tools)

def planner_node(state: AgentState):
    """
    This is the "brain" of the agent.
    It calls the LLM with the current state to decide what to do next.
    """
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools=all_tools)