from pydantic_ai import Agent

'''
Pydantic offers settings.ModelSettings structure to help fine tune the requests made to an agent.
It allows for customisation of common parameters such as temperature, max_tokens, timeout, ...

Approaches:
1. Passing the custom params to the run() via the model_settings arg.
Thus in this case the model can be fine tuned during every request that is made.
2. Passing the custom params during the Agent Initisation also via the model_settings arg.
Thus in this case all the finetuning changes applied to the model persist for every run call.

**Important**
- In approach 2. we can override the settings by passing custom params through the model_settings param
in the run call later in the code.'''

# agent = Agent(
#     model="google-gla:gemini-1.5-flash"
# )

# # Approach 1.
# result_sync = agent.run_sync(
#     "What is the capitial city of Andhra Pradesh ?",
#     model_settings={"temperature":0.9}
# )

# Approach 2.
agent = Agent(
    model="google-gla:gemini-2.0-flash-exp",
    model_settings={"max_tokens":20, "temperature":0.9}
)

result_sync = agent.run_sync(
    "What is the status of the IndianGP in the MotoGP calendar"
)

print(result_sync.data)
