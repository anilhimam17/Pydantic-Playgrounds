from pydantic_ai import Agent, RunContext

"""
Agents in Pydantic act as the wrapper for interacting with LLM's
args:
System Prompt: A set of instructions for the LLM written by the developer.
Function Tools: Functions that the LLM may call to get information while generating a response.
Structured Result Type: The structured datatype the LLM must return at the end of a run, if specified.
Dependancy Type Constraint: System prompt functions, tools, and result validators may all use dependencies when they're run.
LLM Model: Optional default LLM model associated with the agent. Can also be specified when running the agent.
Model Settings: Optional default model settings to help fine tune requests. Can also be specified when running the agent.
"""

# Defining an agent to play roulette
roulette_agent = Agent(
    model="google-gla:gemini-1.5-flash",
    deps_type=int,
    result_type=str,
    system_prompt=(
        "Use the roulette_wheel function to see if the "
        "customer has won based on the number they provide."
    )
)

# Agent Tool
@roulette_agent.tool
async def roulette_wheel(ctx: RunContext[int], square: int) -> str:
    return "Winner" if square == ctx.deps else "Loser"

# Target Variable aka Number Dependancy
success_number = 17

# Queries
result_pass = roulette_agent.run_sync(
    "Heya, prepare the jackpot now I know the answer it seventeen right ?",
    deps=success_number
)
print(result_pass.data)

result_also_pass = roulette_agent.run_sync(
    "Oh, is the answer twenty five - eight", 
    deps=success_number
)
print(result_also_pass.data)

'''
- agent.run(): A coroutine which returns a RunResult containing the completed response.
- agent.run_sync(): A synchronous function which returns a RunResult containing a completed respone.
- agent.run_stream(): A coroutine which returns a StreamedRunResult which contains methods to stream a response as an async iterable.
'''

