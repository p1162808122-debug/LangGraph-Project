from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

from .nodes import finish_node, prepare_node, process_node
from .state import AgentState


def build_graph():
    """Build and compile the learning graph."""
    builder = StateGraph(AgentState)

    builder.add_node("prepare", prepare_node)
    builder.add_node("process", process_node)
    builder.add_node("finish", finish_node)

    builder.add_edge(START, "prepare")
    builder.add_edge("prepare", "process")
    builder.add_edge("process", "finish")
    builder.add_edge("finish", END)

    checkpointer = InMemorySaver()
    return builder.compile(checkpointer=checkpointer)
