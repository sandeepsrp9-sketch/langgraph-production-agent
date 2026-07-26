from langchain_core.messages import AIMessage

from config import llm
from tools import tools


# Bind all tools to the LLM
llm_with_tools = llm.bind_tools(tools)


def chatbot(state):
    """
    Main chatbot node.

    Receives the conversation history,
    invokes the LLM with tool support,
    and returns the AIMessage.
    """

    # Get all conversation messages
    messages = state["messages"]

    # Invoke the LLM
    response = llm_with_tools.invoke(messages)

    # Return the response to LangGraph
    return {
        "messages": [response]
    }