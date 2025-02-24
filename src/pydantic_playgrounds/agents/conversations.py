from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from sys import argv

if len(argv) > 1:
    ollama_model = OpenAIModel(
        argv[1], base_url="http://localhost:11434/v1", api_key="No API Key here !!!!"
    )
    agent = Agent(ollama_model)
else:
    agent = Agent("google-gla:gemini-2.0-flash-exp")

# Carrying out a conversation
result_1 = agent.run_sync("What is the Capital of French Polynesia ?")
print("\n\n", result_1.data, end="\n")
print(result_1.usage())

result_2 = agent.run_sync("What is it famous for ?", message_history=result_1.new_messages())
print("\n\n", result_2.data, end="\n")
print(result_2.usage())
