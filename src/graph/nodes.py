from .state import AgentState


def prepare_node(state: AgentState) -> dict:
    """Step 1: mark the workflow as prepared."""
    return {"step": 1, "history": ["prepare"]}


def process_node(state: AgentState) -> dict:
    """Step 2: process the input message."""
    return {
        "step": 2,
        "result": f"Processed: {state['message']}",
        "history": ["process"],
    }


def finish_node(state: AgentState) -> dict:
    """Step 3: mark the workflow as finished."""
    return {
        "step": 3,
        "result": f"{state['result']} -> Finished",
        "history": ["finish"],
    }
