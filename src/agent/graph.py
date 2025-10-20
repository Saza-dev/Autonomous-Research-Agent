from langgraph.graph import StateGraph, END
from .state import AgentState
from .nodes import planner_node, tool_node
from typing import Literal


def should_continue(state: AgentState) -> Literal["call_tools", "__end__"]:
    """
    This function is our "conditional edge".
    It decides whether to loop back to the 'tool_executor_node' or to end.
    """

    last_message = state['messages'][-1]
    if last_message.tool_calls:
        return "call_tools"
    return END

graph = StateGraph(AgentState)

graph.add_node("planner", planner_node)
graph.add_node("tools",tool_node)

graph.set_entry_point("planner")
graph.add_conditional_edges(
    "planner",
    should_continue,
    {
        "call_tools": "tools", 
        END: END 
    }
)


graph.add_edge("tools", "planner")

app = graph.compile()