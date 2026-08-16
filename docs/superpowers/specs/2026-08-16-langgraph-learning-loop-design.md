# LangGraph Learning Loop Design

## Goal

Create a minimal, directly runnable LangGraph learning project that does not require an LLM or API key. The project should make the core concepts visible: State, Node, Edge, compile, invoke, checkpoint, and multiple graph steps.

## Scope

The first version intentionally does not include LLM calls, RAG, tools, databases, MCP, Send/PUSH tasks, or other advanced features.

## Project Structure

```text
LangGraph-Project/
├── main.py
├── requirements.txt
├── README.md
└── src/graph/
    ├── __init__.py
    ├── state.py
    ├── nodes.py
    └── workflow.py
```

## Graph Structure

```text
START
  ↓
prepare_node
  ↓
process_node
  ↓
finish_node
  ↓
END
```

## State

Use one TypedDict state shared across the graph:

- `message: str` — initial business input.
- `step: int` — shows that each node can update state.
- `result: str` — stores the processed result.

Each node reads the current state and returns only the fields it updates.

## Nodes

### prepare_node

Receives the initial state, increments `step`, and prints the current state so the learner can observe the first node execution.

### process_node

Reads `message`, produces a simple deterministic result, increments `step`, and prints the current state.

### finish_node

Adds a final marker to `result`, increments `step`, and prints the current state.

## Workflow

`workflow.py` creates a `StateGraph(AgentState)`, registers the three nodes, connects them with explicit edges from START to END, then calls `compile()`.

The compiled graph uses an in-memory checkpointer so checkpoint behavior can be demonstrated without a database.

## Runtime

`main.py` is the single learning entry point. It:

1. Builds the compiled graph.
2. Creates initial state data.
3. Provides a `thread_id` in the config so the checkpointer can associate state with one execution thread.
4. Calls `invoke()`.
5. Prints the final state.
6. Reads the saved graph state for the same `thread_id` and prints it, making checkpoint behavior observable.

## Dependencies

Keep dependencies minimal. The first version only needs LangGraph itself; no model SDK or API key is required.

## Success Criteria

After cloning the repository, the learner can create a Python virtual environment, install `requirements.txt`, run `python main.py`, and see all three nodes execute in order, see State change between nodes, see the final State, and see a checkpointed State associated with the configured thread.
