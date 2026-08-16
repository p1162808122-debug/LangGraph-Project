from src.graph.workflow import build_graph


def main() -> None:
    graph = build_graph()

    config = {"configurable": {"thread_id": "demo-thread"}}
    initial_state = {
        "message": "hello LangGraph",
        "step": 0,
        "result": "",
        "history": [],
    }

    print("Initial state:")
    print(initial_state)

    final_state = graph.invoke(initial_state, config=config)

    print("\nFinal state:")
    print(final_state)

    print("\nCheckpoint history (oldest -> newest):")
    snapshots = list(graph.get_state_history(config))
    for index, snapshot in enumerate(reversed(snapshots), start=1):
        print(f"{index}: values={snapshot.values}, next={snapshot.next}")


if __name__ == "__main__":
    main()
