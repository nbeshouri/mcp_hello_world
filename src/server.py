from fastmcp import FastMCP, Context

mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


@mcp.tool()
async def generate_poem(topic: str, ctx: Context) -> str:
    message = await ctx.sample(
        messages=[f"Write a poem about {topic}."],
        system_prompt="You are helpful poet that writes like Yoda.",
    )
    return message.text


if __name__ == "__main__":
    mcp.run()
