from datetime import datetime

from langchain_core.tools import tool

from langchain_tavily import TavilySearch
import os

# ==========================================
# Calculator Tool
# ==========================================

@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.

    Example:
    expression = "25 * 10"
    """

    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Calculation Error: {e}"


# ==========================================
# Current Date & Time Tool
# ==========================================

@tool
def current_datetime() -> str:
    """
    Get the current date and time.
    """

    now = datetime.now()

    return now.strftime("%d-%m-%Y %I:%M:%S %p")

# ==========================================
# Tavily Search Tool
# ==========================================

search_tool = TavilySearch(
    max_results=3,
    api_key=os.getenv("TAVILY_API_KEY"),
)

tools = [
    calculator,
    current_datetime,
    search_tool,
]