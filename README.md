# LangGraph-Project

一个用于学习 LangGraph 核心运行流程的最小可执行项目。

不使用 LLM、RAG、Tool 或 API Key，重点只学习：

```text
State → Node → Edge → compile → invoke → checkpoint
```

## 项目结构

```text
LangGraph-Project/
├── main.py                 # invoke()：启动一次 Graph 执行
├── requirements.txt
├── src/graph/
│   ├── state.py            # State + history reducer（Channel 合并规则）
│   ├── nodes.py            # prepare / process / finish 三个 Node
│   └── workflow.py         # Edge + compile + InMemorySaver
└── tests/
    ├── test_nodes.py
    └── test_workflow.py
```

Graph 的执行结构：

```text
START
  ↓
prepare
  ↓
process
  ↓
finish
  ↓
END
```

## 本地运行

```bash
git clone https://github.com/p1162808122-debug/LangGraph-Project.git
cd LangGraph-Project

python3 -m venv .venv
source .venv/bin/activate

python -m pip install -r requirements.txt
python main.py
```

运行后可以看到：

1. 初始 State
2. 三个 Node 执行后的最终 State
3. Checkpoint 保存的 State 历史

## 运行测试

```bash
pytest -q
```

## 学习时重点看哪里

### `state.py`

`AgentState` 定义整个 Graph 共享的数据结构。`history` 使用 reducer，把各个 Node 写入的列表合并起来。

### `nodes.py`

每个 Node 本质上都是函数：读取当前 State，返回需要更新的部分 State。

### `workflow.py`

这里负责：

```text
创建 StateGraph
→ 注册 Node
→ 添加 Edge
→ 配置 Checkpoint
→ compile()
```

### `main.py`

这里通过：

```python
graph.invoke(initial_state, config=config)
```

真正启动已经 compile 好的 Graph。

## 和你学过的 Pregel 底层知识怎么对应

你不会在这个项目里直接调用 `PregelLoop`、`tick()`、`put_writes()`、`apply_writes()`。

它们属于 LangGraph 内部 Runtime。你调用 `invoke()` 后，底层才会用这些机制把 Graph 按多个 Super Step 一轮一轮执行。

这个项目先从上层 API 看懂完整执行链，再逐步往 Pregel 源码下钻。
