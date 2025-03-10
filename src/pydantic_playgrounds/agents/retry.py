from pydantic_ai import Agent, ModelRetry, RunContext
from pydantic import BaseModel
import pandas as pd


class User(BaseModel):
    name: str
    age: int
    email: list[str]


# Input Deps
df = pd.DataFrame({
    "name": ["Anil", "Sandeep", "Pratik", "Nikhil", "Vignesh"],
    "age": [22, 21, 20, 20, 21],
    "email": ["ag@gmail.com", "sr@hotmail.com", "pk@googlemail.com", "nb@yahoo.com", "vm@msn.com"]
})

# Agent Declaration
agent = Agent(
    "google-gla:gemini-1.5-flash", deps_type=pd.DataFrame, result_type=User,
    system_prompt="use search_user() to search for the user in the database."
)


# Providing retries for the function tool used by the Agent
@agent.tool(retries=2)
def search_user(ctx: RunContext[pd.DataFrame], name: str) -> User:
    df = ctx.deps
    df_search = df[df["name"] == name]

    if df_search.empty:
        raise ModelRetry(f"User with name {name} was not found")

    return User(
        name=df_search["name"].iloc[0],
        age=df_search["age"].iloc[0],
        email=[df_search["email"].iloc[0]]
    )


result = agent.run_sync(
    "Do we know someome by the name of Krisha, what is his email id ?", deps=df
)
print(result.data)
