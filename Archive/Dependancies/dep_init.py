from dataclasses import dataclass
from pydantic_ai import Agent
import httpx
import asyncio

"""
- Passing dependancies to pydantic-ai models plays a key role in querying the 
agents through prompts. However, by default dependencies are passed to 
pydantic-ai models are singular and don't have complex structures.

**Enter Dataclasses**
- Dataclasses from pydantic can be used to create complex structures which 
can structure the outputs produced by the model while also providing data 
validation for all the outputs provided by the model.
"""


# Dataclass definition
@dataclass
class MyDeps:
    api_key: str
    http_client: httpx.AsyncClient


# Agent Initialisation
agent = Agent(
    "google-gla:gemini-1.5-flash",
    deps_type=MyDeps
)


# Driver Function
async def main():
    async with httpx.AsyncClient() as client:
        deps = MyDeps("foobar", client)
        result = await agent.run(
            "Tell me a joke.", deps=deps
        )
        print(result.data)

"""
Just calling the main() doesnt work in this case as the main() requires 
an event loop to trigger the program and make the corresponding API 
requests.
"""
asyncio.run(main())
