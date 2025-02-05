from dataclasses import dataclass
from pydantic_ai import Agent, RunContext
import asyncio
import httpx


@dataclass
class MyDeps:
    api_key: str
    http_client: httpx.AsyncClient


agent = Agent(
    "google-gla:gemini-1.5-flash",
    deps_type=MyDeps
)


# Accessing the Dependancy
@agent.system_prompt
async def get_system_prompt(ctx: RunContext[MyDeps]) -> str:
    response = await ctx.deps.http_client.get(
        "https://example.com",
        # Asynchronous Dependancy Injection
        headers={"Authorization": f"Bearer {ctx.deps.api_key}"} 
    )
    response.raise_for_status()
    return f"Prompt: {response.text}"


async def main():
    async with httpx.AsyncClient() as client:
        deps = MyDeps("foobar", client)
        result = await agent.run(
            "Tell me a joke now ?", deps=deps
        )

        print(result.data)

asyncio.run(main())

"""
Flow of the program:
- A httpx request a made to a dummy website using the predefined dependancy dataclass.
- The response retreived from the website forms the system prompt for the AI model.
- The system prompt is passed automatically to the ai agent through the decorator.

The program then resumes normal data flow when making requests to the
 Pydantic AI model to query the agent.
"""
