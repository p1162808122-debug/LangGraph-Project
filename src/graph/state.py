from typing import TypedDict


class AgentState(TypedDict):
    """State passed between LangGraph nodes."""

    message: str
    result: str
