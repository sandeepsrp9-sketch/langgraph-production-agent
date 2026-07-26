import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq


# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()


# ==========================================
# Large Language Model
# ==========================================

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
)