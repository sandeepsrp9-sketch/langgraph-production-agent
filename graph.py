from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition

from state import AgentState
from chatbot import chatbot
from tools import tools


# Create the graph builder
builder = StateGraph(AgentState)

# Create ToolNode
tool_node = ToolNode(tools)

# Add nodes
builder.add_node("chatbot", chatbot)
builder.add_node("tools", tool_node)

# Start the graph
builder.add_edge(START, "chatbot")

# Conditional routing
builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)

# Return from ToolNode back to chatbot
builder.add_edge(
    "tools",
    "chatbot",
)

# Compile the graph
app = builder.compile()