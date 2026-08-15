from src.graph.workflow import build_graph


if __name__ == "__main__":
    graph = build_graph()

    result = graph.invoke({
        "message": "Hello LangGraph",
        "result": ""
    })

    print(result)
