# MCP Hello, World!

## Running

1. Run `uv sync` to create a virtual environment. 
2. Remove the `.example` from `.env.example` and either add your OpenAI key or change the model type to a local model that works with tools (e.g. `MODEL_PROVIDER=ollama` and `MODEL=llama3.1`).
3. Run `uv run src/client.py`
4. Ask it to write you a poem or multiply some numbers.