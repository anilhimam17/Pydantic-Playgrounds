from dataclasses import dataclass, field
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from sys import argv

SYSTEM_PROMPT = """
Use the `roulette_wheel` function to see if the customer has won based
on the number they have provided as input.
"""

if len(argv) > 1:
    # Declaring the Agent running locally using Ollama
    ollama_agent = OpenAIModel(
        argv[1], base_url="http://localhost:11434/v1", api_key="Heya, no API key here!!!"
    )

    # Constructing an instance of the Pydantic-AI agent object
    roulette_agent = Agent(
        ollama_agent, deps_type=int, result_type=bool, system_prompt=SYSTEM_PROMPT
    )
else:
    roulette_agent = Agent(
        "google-gla:gemini-2.0-flash-exp", deps_type=int, result_type=bool, system_prompt=SYSTEM_PROMPT
    )


@roulette_agent.tool
async def roulette_wheel(ctx: RunContext[int], square: int) -> str:
    return "Winner" if square == ctx.deps else "Loser"


# Running the Agent Query
success_number = 17
result = roulette_agent.run_sync("Put my money on teen", deps=success_number)
print(result.data)
