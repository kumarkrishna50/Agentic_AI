from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "weather": {
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable-http"
            }
        }
    )

    import os
    from dotenv import load_dotenv
    load_dotenv()
    tools =await client.get_tools()

    from langchain_google_genai import ChatGoogleGenerativeAI
    llm = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

    agent = create_agent(model=llm, tools=tools)
    hello_response = await agent.ainvoke({"messages": [{"role": "user", "content": "Hello!"}]})
    print(hello_response)

    weather_response = await agent.ainvoke({"messages": [{"role": "user", "content": "What is the weather like today?"}]})
    print(weather_response)

asyncio.run(main())