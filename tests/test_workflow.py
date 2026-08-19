from src.graph.workflow import build_graph


def test_graph_runs_through_all_nodes():
    graph = build_graph()
    config = {"configurable": {"thread_id": "test-run"}}

    result = graph.invoke(
        {"message": "hello", "step": 0, "result": "", "history": []},
        config=config,
    )

    assert result == {
        "message": "hello",
        "step": 3,
        "result": "Processed: hello -> Finished",
        "history": ["prepare", "process", "finish"],
    }


def test_checkpoint_history_is_saved():
    graph = build_graph()
    config = {"configurable": {"thread_id": "checkpoint-run"}}

    graph.invoke(
        {"message": "hello", "step": 0, "result": "", "history": []},
        config=config,
    )

    snapshots = list(graph.get_state_history(config))

    assert len(snapshots) >= 4
    assert snapshots[0].values["step"] == 3
