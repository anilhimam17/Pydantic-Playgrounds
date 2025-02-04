from pydantic_ai import Agent
from pydantic_ai.exceptions import UsageLimitExceeded
from pydantic_ai.usage import UsageLimits

# Agent Initialisation
agent = Agent(
    model="google-gla:gemini-1.5-flash"
)

# Prompt Query
# result_sync = agent.run_sync(
#     "What is the capital city of Scotland ? Answer within a single line.",
#     usage_limits=UsageLimits(response_tokens_limit=30)
# )

# print("API Response:\n", result_sync.data)
# print("\nAPI Usage Metric:\n", result_sync.usage())

# Prompt Limit Exceeded
try:
    result_sync = agent.run_sync(
        user_prompt=(
            "What is the captial city of Scotland ?"
            "Provide in bullet points why it might be famous ?"
            "Try to keep it concise too."
        ),
        usage_limits=UsageLimits(response_tokens_limit=10)
    )
except UsageLimitExceeded as e:
    print(e)
