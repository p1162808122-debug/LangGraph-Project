from operator import add
from typing import Annotated, TypedDict


class AgentState(TypedDict):
    """Shared state that flows through the LangGraph workflow."""

    message: str
    step: int
    result: str
    # LangGraph uses this reducer to merge each node's history update.
    history: Annotated[list[str], add]
