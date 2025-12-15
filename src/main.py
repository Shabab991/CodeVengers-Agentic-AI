from agent_planner import plan_tasks
from agent_executor import execute_tasks
from agent_reflector import reflect


if __name__ == "__main__":
goal = input("Enter your goal: ")
print("
--- Planning ---")
plan = plan_tasks(goal)
print(plan)


print("
--- Executing ---")
result = execute_tasks(plan)
print(result)


print("
--- Reflecting ---")
final = reflect(result)
print(final)
