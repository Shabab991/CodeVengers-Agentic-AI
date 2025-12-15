from utils import get_model


def execute_tasks(task_plan: str):
model = get_model()
prompt = f"""
You are an execution agent.
Given the task plan below, simulate execution and produce results for each step.


Task Plan:
{task_plan}
"""
response = model.generate_content(prompt)
return response.text
