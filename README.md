# 🤖 LangGraph Production Agent

A production-style AI Agent built using **LangGraph**, **LangChain**, **Groq LLM**, and **Tavily Search**.

This project demonstrates how to build an intelligent AI assistant capable of:

- Answering general questions
- Performing mathematical calculations
- Providing the current date and time
- Searching the web for real-time information
- Automatically deciding when to use tools through LangGraph

---

#  Features

- ✅ LangGraph StateGraph Workflow
- ✅ Tool Calling with LangChain
- ✅ Calculator Tool
- ✅ Current Date & Time Tool
- ✅ Tavily Web Search Tool
- ✅ Automatic Tool Selection
- ✅ Conversation Memory using `thread_id`
- ✅ Streaming Responses
- ✅ Modular Project Structure

---

#  Project Structure

```text
langgraph-production-agent/
│
├── app.py              # Entry point of the application
├── graph.py            # Builds the LangGraph workflow
├── chatbot.py          # Chatbot node with LLM and tool binding
├── tools.py            # Custom tools (Calculator, DateTime, Tavily Search)
├── state.py            # Agent state definition
├── config.py           # LLM configuration
├── requirements.txt    # Project dependencies
├── .gitignore
├── .env.example
└── README.md
```

---

#  Installation

## 1. Clone the Repository

```bash
git clone https://github.com/sandeepsrp9-sketch/langgraph-production-agent.git
```

Go into the project folder:

```bash
cd langgraph-production-agent
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

#  Usage

Run the application:

```bash
python app.py
```

You should see:

```text
============================================================
 Production Agentic AI Assistant
Type 'exit' to quit
============================================================
```

Example questions:

```text
What is 25 * 45?

What's today's date?

Search latest AI news.

Who is the CEO of Microsoft?

exit
```

---

#  Architecture

```text
                   User
                     │
                     ▼
               HumanMessage
                     │
                     ▼
               LangGraph App
                     │
                     ▼
              +--------------+
              |   Chatbot    |
              +--------------+
                     │
                     ▼
             llm_with_tools.invoke()
                     │
                     ▼
                AIMessage
             (tool_calls?)
               │        │
              Yes      No
               │        │
               ▼        ▼
         +-------------+ END
         |  ToolNode   |
         +-------------+
               │
               ▼
   Calculator / Date / Tavily
               │
               ▼
          ToolMessage
               │
               ▼
          +-------------+
          |  Chatbot    |
          +-------------+
               │
               ▼
          Final Response
```

---

#  Sample Output

### Example 1 – Calculator

**User**

```text
What is 125 × 16?
```

**Assistant**

```text
The answer is 2000.
```

---

### Example 2 – Date & Time

**User**

```text
What is today's date?
```

**Assistant**

```text
Today's date is 26 July 2026.
```

---

### Example 3 – Web Search

**User**

```text
Latest AI news
```

**Assistant**

```text
Here are the latest developments in AI...
```



#  Technologies Used

| Technology     | Purpose |

| Python         | Programming Language |
| LangGraph      | Agent Workflow |
| LangChain      | LLM Framework |
| Groq           | Large Language Model |
| Tavily Search  | Real-time Web Search |
| python-dotenv  | Environment Variable Management |



#  Concepts Demonstrated

- StateGraph
- Agent State
- Tool Calling
- ToolNode
- tools_condition
- add_messages Reducer
- Conditional Edges
- Conversation Memory
- Streaming Execution
- LangChain Tools
- Modular Project Design


#  Future Improvements

- Add RAG (Retrieval-Augmented Generation)
- Add PDF Question Answering
- Add Memory Persistence
- Add Multi-Agent Architecture
- Build a Streamlit Web Interface
- Docker Support
- Deploy to Cloud

---

#  Author

**Sandeep Kumar Reddy Konireddy**

GitHub: https://github.com/sandeepsrp9-sketch

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.
