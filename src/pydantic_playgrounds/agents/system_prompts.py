from pydantic_ai import Agent, RunContext
from datetime import date

agent = Agent(
    "google-gla:gemini-1.5-flash", deps_type=str, result_type=str,
    system_prompt="use the customer name when responding"
)


@agent.system_prompt
def add_user_name(ctx: RunContext[str]) -> str:
    return f"The users name is {ctx.deps}"


@agent.system_prompt
def add_the_date() -> str:
    return f"The date today is {date.today()}"


result = agent.run_sync("Heya what is the date today ?", deps="Anil")
print(result.data)
