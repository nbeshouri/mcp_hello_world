import os, sys
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Tell the client how to launch your server:
server_params = StdioServerParameters(
    command=sys.executable,      # e.g. /usr/bin/python3
    args=["src/server.py"],          # your server script
    env=os.environ.copy(),       # inherit whatever env you need
)

async def run():
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()

            # now you can list and call your tools/resources
            tools = await session.list_tools()
            print("Tools:", tools)

            # example: call your add tool
            result = await session.call_tool("add", {"a": 2, "b": 3})
            print("2 + 3 =", result)

            greeting = await session.read_resource("greeting://Alice")
            print(greeting)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())