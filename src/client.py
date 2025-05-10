import asyncio

from dotenv import load_dotenv
from fastmcp import Client
from fastmcp.client.sampling import RequestContext, SamplingMessage, SamplingParams
from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent


load_dotenv()
model = init_chat_model(model="gpt-4o-mini", model_provider="openai")


async def main():
    async with Client("src/server.py", sampling_handler=sampling_handler) as client:
        tools = await load_mcp_tools(client.session)
        memory = MemorySaver()

        agent = create_react_agent(model, tools, checkpointer=memory)

        thread_id = "chat_session"

        while True:
            user_input = input(">> ").strip()
            if user_input.lower() in {"exit", "quit"}:
                print("Exiting...")
                break

            try:
                final_state = await agent.ainvoke(
                    {"messages": [{"role": "user", "content": user_input}]},
                    config={"configurable": {"thread_id": thread_id}},
                )

                last_response = final_state["messages"][-1].content
                print(last_response)

            except Exception as e:
                print("Error processing input:", e)


async def sampling_handler(
    messages: list[SamplingMessage], params: SamplingParams, context: RequestContext
) -> str:
    formatted_messages = []
    formatted_messages.append({"role": "system", "content": params.systemPrompt})
    for message in messages:
        formatted_messages.append(
            {"role": message.role, "content": message.content.text}
        )

    response = await model.ainvoke(formatted_messages, max_tokens=params.maxTokens)

    return response.content


if __name__ == "__main__":
    asyncio.run(main())
