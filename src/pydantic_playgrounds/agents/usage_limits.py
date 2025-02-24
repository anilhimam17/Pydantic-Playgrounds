from pydantic_ai import Agent
from pydantic_ai.exceptions import UsageLimitExceeded
from pydantic_ai.usage import UsageLimits

agent = Agent("google-gla:gemini-2.0-flash-exp")

result = agent.run_sync(
    user_prompt="What is the capital of Andhra Pradesh ?",
    usage_limits=UsageLimits(response_tokens_limit=50)
)

print(result.data)
print(result.usage())

try:
    result_para = agent.run_sync(
        "What is Andhra Pradesh famous for ? answer in detail.",
        usage_limits=UsageLimits(total_tokens_limit=20)
    )
except UsageLimitExceeded as e:
    print(e)
