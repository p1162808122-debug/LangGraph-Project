from src.graph.nodes import finish_node, prepare_node, process_node


def test_prepare_node_starts_workflow():
    state = {"message": "hello", "step": 0, "result": "", "history": []}
    assert prepare_node(state) == {"step": 1, "history": ["prepare"]}


def test_process_node_builds_result():
    state = {"message": "hello", "step": 1, "result": "", "history": ["prepare"]}
    assert process_node(state) == {"step": 2, "result": "Processed: hello", "history": ["process"]}


def test_finish_node_marks_completion():
    state = {"message": "hello", "step": 2, "result": "Processed: hello", "history": ["prepare", "process"]}
    assert finish_node(state) == {"step": 3, "result": "Processed: hello -> Finished", "history": ["finish"]}
