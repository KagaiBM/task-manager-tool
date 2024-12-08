# add_task.py
def add_task(tasks, task):
    tasks.append(task)
    return tasks

tasks = []
task = input("Enter a new task: ")
tasks = add_task(tasks, task)
print("Tasks:", tasks)
