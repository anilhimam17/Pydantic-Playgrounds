from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from sys import argv

MODEL_SETTINGS = {"temperature": 0.3, "max_tokens": 30}

if len(argv) > 1:
    ollama_model = OpenAIModel(
        argv[1], base_url="http://localhost:11434/v1", api_key="No API Key here !!!!"
    )
    agent = Agent(
        ollama_model, model_settings=MODEL_SETTINGS
    )
else:
    agent = Agent(
        "google-gla:gemini-2.0-flash-exp", model_settings=MODEL_SETTINGS
    )

# Running the Query
result = agent.run_sync(
    "Heya, what is the capital city of Brasil ? what is it famous for ?"
)
print(result.data)
print(result.usage())
