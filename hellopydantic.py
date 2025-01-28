import os
from pydantic_ai import Agent

# Gemini API Key
api_key = os.environ.get("GEMINI_API_KEY")

# Instantiating an Agent
agent = Agent(
    model="google-gla:gemini-1.5-flash",
    system_prompt="Keep it simple"
)

# Query Prompt
result = agent.run_sync("Where does the notion of Hello, World come from ?")
print(result.data)
