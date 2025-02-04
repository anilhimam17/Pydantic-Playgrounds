from pydantic_ai import (
    Agent, ModelRetry, UnexpectedModelBehavior, capture_run_messages
)

# Agent Initialisation
agent = Agent(
    "google-gla:gemini-1.5-flash",
    system_prompt=(
        "Provide the polygon name and are are bullet points"
    )
)


@agent.tool_plain
def calc_volume(size: int) -> int:
    """
    A tool_plain decorator is used to decorate tool functions which do not 
    take a RunContext parameter as input.
    """
    if size == 42:
        return size ** 3
    else:
        raise ModelRetry("Please try again")


with capture_run_messages() as messages:
    try:
        result = agent.run_sync("Retrieve the volume of the box \n\
            with size 43 again ?")
    except UnexpectedModelBehavior as e:
        print("An error occured\n", e)
        print("\nCause: ", repr(e.__cause__))
        print("\nMessages: ", messages)
    else:
        print(result.data)
