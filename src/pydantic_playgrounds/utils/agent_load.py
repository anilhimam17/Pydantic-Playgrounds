from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel


def load_ollama_agent(model_name: str) -> Agent:
    ollama_model = OpenAIModel(model_name)
    agent = Agent(ollama_model)

    return agent
