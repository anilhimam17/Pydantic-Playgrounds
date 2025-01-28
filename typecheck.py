from dataclasses import dataclass
from pydantic_ai import Agent, RunContext

'''
By utilising dataclasses pydantic is able to apply type check on data from the get-go:
- Parsing dependancy_type and result_type to the Agent Object during initialisation
- Parsing dependancies to function tools used by the agents.
**Thus if there is any type mismatch the program catches it immediatly without applying 
any implicit type coersion which might cause problems later**
'''

@dataclass
class User:
    name: str

agent = Agent(
    model="google-gla:gemini-1.5-flash", 
    deps_type=User, result_type=bool
)

@agent.system_prompt
def add_user(ctx: RunContext[str]) -> str:
    return f"The user's name is {ctx.deps}"

result = agent.run_sync(
    user_prompt="Heya, does your name start with a Sam ?", deps=User("Gemini")
)
print(result.data)

def byte_convert(x: bytes) -> None:
    pass
print(byte_convert(result.data))