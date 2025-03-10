from dataclasses import dataclass
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from sys import argv


@dataclass
class User:
    name: str


if len(argv) > 1:
    # Agent Initialisation
    ollama_agent = OpenAIModel(
        argv[1], base_url="https://localhost:11434/v1", api_key="no api key!!"
    )

    agent = Agent(
        ollama_agent, deps_type=User, result_type=bool
    )
else:
    agent = Agent(
        "google-gla:gemini-1.5-flash", deps_type=User, result_type=bool
    )


@agent.system_prompt
def add_user_name(ctx: RunContext[User]) -> str:
    return f"The user's name is {ctx.deps.name}."


result = agent.run_sync(
    "Does the name of the user start with A ?", deps=User("Anil")
)
print(result.data)
