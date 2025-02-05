from turtle import heading
from pydantic_ai import Agent, ModelRetry, RunContext
from dataclasses import dataclass
import httpx


# Dependancy Class
@dataclass
class MyDeps:
    api_key: str
    http_client: httpx.AsyncClient


# Agent Intialisation
agent = Agent(
    "google-gla:gemini-1.5-flash",
    deps_type=MyDeps
)


# Runtime Systemprompt Injection
@agent.system_prompt
async def get_system_prompt(ctx: RunContext[MyDeps]) -> str:
    response = await ctx.deps.http_client.get("https://example.com")
    response.raise_for_status()
    return f"Prompt: {response.text}"


@agent.tool
async def get_joke_material(ctx: RunContext[MyDeps], subjects: str) -> str:
    response = await ctx.deps.http_client.get(
        "https://example.com#jokes",
        params={"subject": subjects},
        headers={"Authorization": f"Bearer"}
    )