from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
import asyncio
from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage, AIMessage

model = init_chat_model(model="gpt-4o", model_provider="openai")

server_params = StdioServerParameters(
    command="python",
    args=["src/server.py"],
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)
            
            messages = []
            while True:
                user_input = input(">> ").strip()
                if user_input.lower() in {"exit", "quit"}:
                    print("Exiting...")
                    break
                
                messages.append(("user", user_input))
                
                try:
                    final_state = await agent.ainvoke(
                        {"messages": messages}, 
                    )
                except Exception as e:
                    print("Error processing input:", e)
                    continue
                
                last_response = final_state["messages"][-1].content
                messages.append(("ai", last_response))
                print(last_response)


if __name__ == "__main__":
    asyncio.run(main())