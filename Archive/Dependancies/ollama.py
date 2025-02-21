from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel


class CityLocation(BaseModel):
    city_name: str
    city_location: str
    country: str


# Ollama Model Access
ollama_model = OpenAIModel(
    model_name="deepseek-r1:14b", base_url="http://localhost:11434/"
)

# Agent Initialisation
agent = Agent(
    ollama_model, result_type=CityLocation
)

# Query
result = agent.run_sync(
    user_prompt=(
        "What is the capital of Andhra Pradesh ?"
        "What are its location coordinates and where is it ?"
    )
)

# Metadata
print("Query Result:\n", result.data)
print("\nToken Usage:\n", result.usage())