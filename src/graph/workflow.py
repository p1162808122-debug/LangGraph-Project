from langgraph.graph import StateGraph

from .state import AgentState
from .nodes import process_node


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("process", process_node)
    graph.set_entry_point("process")
    graph.set_finish_point("process")

    return graph.compile()
