from pydantic_ai import Agent

"""
An agent run might represent an entire conversation — there's no limit to 
how many messages can be exchanged in a single run. 
However, a conversation might also be composed of multiple runs, especially 
if you need to maintain state between separate interactions or API calls.

To achieve a back and forth conversation with states preserved we utilise the 
result.new_messages() to the follow-up run() through the message_history parameter.
"""

agent = Agent(
    model="google-gla:gemini-2.0-flash-exp",
    model_settings={"temperature":0.9},
    system_prompt="keep it simple and concise"
)

name_prompt = """
Name an influential person other than Geoff Hinton, 
Yoshua Bengio and Yann Lecun who has significantly 
contributed to the field of modern AI
"""

result_name = agent.run_sync(
    user_prompt=name_prompt
)
print("Result Usage:\n", result_name.usage())
print("Answer:\n", result_name.data)

result_follow_up = agent.run_sync(
    user_prompt="Can you name the places the person you have mentioned has worked ?",
    message_history=result_name.new_messages()
)
print("\nResult Usage:\n", result_follow_up.usage())
print("Answer:\n", result_follow_up.data)

result_final = agent.run_sync(
    user_prompt="Can you name in bullet points what / how the individual has contributed ?",
    message_history=result_follow_up.new_messages()
)
print("\nResult Usage:\n", result_final.usage())
print("Answer:\n", result_final.data)





