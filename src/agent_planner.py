from utils import get_model


def plan_tasks(goal: str):
model = get_model()
prompt = f"""
You are a planning agent.
Break the following goal into clear, ordered, actionable steps.
Return steps as a numbered list.


Goal: {goal}
"""
response = model.generate_content(prompt)
return response.text
