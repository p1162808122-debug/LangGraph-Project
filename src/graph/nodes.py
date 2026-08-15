from .state import AgentState


def process_node(state: AgentState):
    """A simple LangGraph node."""

    return {
        "result": f"Processed: {state['message']}"
    }
