# Minimal LangGraph Learning Loop Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a clone-and-run LangGraph learning project that demonstrates State, Node, Edge, compile, invoke, checkpoints, and multiple graph steps without any LLM or API key.

**Architecture:** Keep the existing `src/graph` structure. A typed state flows through three deterministic nodes (`prepare`, `process`, `finish`) connected by explicit `START`/`END` edges. The graph is compiled with `InMemorySaver`, and `main.py` invokes it with a `thread_id` and prints the final state plus checkpoint history.

**Tech Stack:** Python 3.10+, LangGraph, pytest.

## Global Constraints

- No LLM, RAG, tools, database, or API key.
- Keep the code small enough for a beginner to trace line by line.
- Use explicit `StateGraph`, `START`, `END`, `compile()`, and `invoke()` calls.
- Use `InMemorySaver` only to demonstrate checkpoint behavior.
- The repository must run locally after dependency installation.

---

### Task 1: Define observable state and node behavior

**Files:**
- Modify: `src/graph/state.py`
- Modify: `src/graph/nodes.py`
- Create: `tests/test_nodes.py`

**Interfaces:**
- `AgentState` contains `message: str`, `step: int`, `result: str`, `history: list[str]`.
- `prepare_node(state)`, `process_node(state)`, and `finish_node(state)` each return a partial state update.

- [ ] Write node tests first.
- [ ] Verify the tests fail against the current one-node implementation.
- [ ] Implement the minimal three-node behavior.
- [ ] Verify node tests pass.

### Task 2: Build and compile the graph with checkpointing

**Files:**
- Modify: `src/graph/workflow.py`
- Create: `tests/test_workflow.py`

**Interfaces:**
- `build_graph()` returns a compiled LangGraph graph.
- Graph path: `START -> prepare -> process -> finish -> END`.
- Graph uses `InMemorySaver` as its checkpointer.

- [ ] Write workflow tests first for final state and checkpoint history.
- [ ] Verify the tests fail before workflow changes.
- [ ] Add all nodes, explicit edges, and `InMemorySaver` to `compile()`.
- [ ] Verify workflow tests pass.

### Task 3: Add a runnable entry point and beginner README

**Files:**
- Create: `main.py`
- Modify: `README.md`
- Modify: `requirements.txt`

**Interfaces:**
- Running `python main.py` invokes the graph with a fixed demo input and thread ID.
- Output shows final state and checkpoint history.

- [ ] Add `pytest` to dependencies.
- [ ] Add the runnable example.
- [ ] Document clone, virtual environment, install, run, and test commands.
- [ ] Run `pytest -q` and `python main.py` as final verification.
