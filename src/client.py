from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
import asyncio
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver

model = init_chat_model(model="gpt-4o-mini", model_provider="openai")

server_params = StdioServerParameters(
    command="python",
    args=["src/server.py"],
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            
            await session.initialize()
            tools = await load_mcp_tools(session)
            memory = MemorySaver()
            
            agent = create_react_agent(
                model, 
                tools,
                checkpointer=memory
            )
            
            thread_id = "chat_session"
            
            while True:
                user_input = input(">> ").strip()
                if user_input.lower() in {"exit", "quit"}:
                    print("Exiting...")
                    break
                
                try:
                    final_state = await agent.ainvoke(
                        {"messages": [{"role": "user", "content": user_input}]},
                        config={"configurable": {"thread_id": thread_id}}
                    )
                    
                    last_response = final_state["messages"][-1].content
                    print(last_response)
                    
                except Exception as e:
                    print("Error processing input:", e)

if __name__ == "__main__":
    asyncio.run(main())