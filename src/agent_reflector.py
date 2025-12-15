from utils import get_model


def reflect(execution_result: str):
model = get_model()
prompt = f"""
You are a reflection agent.
Evaluate the execution result below and suggest improvements or confirm success.


Execution Result:
{execution_result}
"""
response = model.generate_content(prompt)
return response.text
