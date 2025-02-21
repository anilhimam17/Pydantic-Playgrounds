from pydantic import BaseModel
from pydantic_ai import Agent, RunContext, ModelRetry
import pandas as pd


class ChatResult(BaseModel):
    user_id: int
    message: str


# Agent Initialisation
agent = Agent(
    "google-gla:gemini-1.5-flash",
    deps_type=pd.DataFrame,
    result_type=ChatResult
)


# Agent Tool
@agent.tool(retries=2)
def get_user_by_name(ctx: RunContext[pd.DataFrame], name: str) -> int:
    print("User to query: ", name)

    df = ctx.deps
    matching = df[df["name"] == name]

    if matching.empty:
        raise ModelRetry(
            f"No user found with {name}, please provide their full name."
        )

    user_id = int(matching.iloc[0]["user_id"])
    return user_id


# User Dataframe
user_df = pd.DataFrame({
    "user_id": [1, 2, 3],
    "name": ["Sandeep", "Pratik", "Sai"],
    "base": ["Chennai", "Madurai", "Banglore"]
})

result = agent.run_sync(
    user_prompt="Send a message to Sai asking \n\
        if he has worked with transformers previously ?\n\
        also ask her where she is based from to see if she work from office.",
    deps=user_df
)
print(result.data)
