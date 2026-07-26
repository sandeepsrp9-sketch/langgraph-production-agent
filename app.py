from langchain_core.messages import HumanMessage

from graph import app


config = {
    "configurable": {
        "thread_id": "production-agent"
    }
}


print("=" * 60)
print("🤖 Production Agentic AI Assistant")
print("Type 'exit' to quit")
print("=" * 60)


while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    events = app.stream(
        {
            "messages": [
                HumanMessage(content=user_input)
            ]
        },
        config=config,
        stream_mode="values",
    )

    for event in events:
        event["messages"][-1].pretty_print()