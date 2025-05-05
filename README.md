
# LangGraph Functional API

LangGraph's Functional API enables developers to build stateful, multi-agent, and graph-based workflows using standard Python functions. It offers features like persistence, memory management, human-in-the-loop interactions, and streaming, all without the need to define explicit graph structures.

---

## 🔧 Overview

The Functional API is designed to integrate seamlessly with existing Python codebases, allowing developers to incorporate LangGraph's capabilities with minimal modifications. It leverages two primary decorators:

* **@entrypoint**: Marks the starting point of a workflow, managing execution flow, state persistence, and handling long-running tasks and interrupts.

* **@task**: Defines discrete units of work that can be executed asynchronously within an entrypoint. Tasks return future-like objects that can be awaited or resolved synchronously.

This design enables developers to use familiar programming constructs like loops and conditionals to control workflow execution.&#x20;

---

## ✅ Installation

To install LangGraph, use pip:

```bash
pip install langgraph
```

---

## 📌 Defining Functional Workflows

### 1. Defining a Task

Tasks represent individual units of work within a workflow.

```python
from langgraph.func import task

@task
def write_essay(topic: str) -> str:
    """Write an essay about the given topic."""
    # Simulate a long-running task
    time.sleep(1)
    return f"An essay about {topic}"
```

### 2. Defining an Entrypoint

Entrypoints serve as the starting point of workflows, orchestrating tasks and managing state.

```python
from langgraph.func import entrypoint
from langgraph.checkpoint.memory import MemorySaver

@entrypoint(checkpointer=MemorySaver())
def workflow(topic: str) -> dict:
    """A simple workflow that writes an essay."""
    essay = write_essay(topic).result()
    return {"essay": essay}
```

In this example, `MemorySaver` is used to enable state persistence across workflow executions.

---

## 📚 Resources

* [LangGraph GitHub Repository](https://github.com/langchain-ai/langgraph)
* [Functional API Documentation](https://langchain-ai.github.io/langgraph/concepts/functional_api/)
* [LangGraph Functional API Blog Post](https://blog.langchain.dev/introducing-the-langgraph-functional-api/)
* [LangGraph Functional API Video Tutorial](https://www.youtube.com/watch?v=NXhyWJozM8A)

---

