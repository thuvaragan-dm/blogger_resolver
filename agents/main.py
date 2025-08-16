# architecture.py

from langgraph.graph import StateGraph, END
from typing import TypedDict

# Define shared state
class AgentState(TypedDict):
    topics: str
    draft: str
    edited_post: str
    published: bool

# Dummy agent implementations (can be LangChain LLMs in real case)
def topic_extractor(state: AgentState) -> AgentState:
    print("🔍 topic_extractor running...")
    return {**state, "topics": "AI, Productivity, Writing"}

def content_writer(state: AgentState) -> AgentState:
    print("✍️ content_writer running...")
    return {**state, "draft": "This is a blog draft on AI productivity tools."}

def editor(state: AgentState) -> AgentState:
    print("📝 editor running...")
    return {**state, "edited_post": "Final edited version of the blog post."}

def publisher(state: AgentState) -> AgentState:
    print("📤 publisher running...")
    return {**state, "published": True}

# Build the LangGraph
def get_graph():
    graph = StateGraph(AgentState)

    graph.add_node("topic_extractor", topic_extractor)
    graph.add_node("content_writer", content_writer)
    graph.add_node("editor", editor)
    graph.add_node("publisher", publisher)

    graph.set_entry_point("topic_extractor")
    graph.add_edge("topic_extractor", "content_writer")
    graph.add_edge("content_writer", "editor")
    graph.add_edge("editor", "publisher")
    graph.add_edge("publisher", END)

    return graph.compile()

# Run example
if __name__ == "__main__":
    app = get_graph()
    final_state = app.invoke({})
    print("\n✅ Final State:\n", final_state)
