# delete_task.py
def delete_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
    return tasks

tasks = ["Task 1", "Task 2"]
task = input("Enter task to delete: ")
tasks = delete_task(tasks, task)
print("Tasks:", tasks)
