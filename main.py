# main.py
def add_task(task_list, task_description):
    task_list.append(task_description)
    print(f"Task '{task_description}' added.")

if __name__ == "__main__":
    tasks = []
    print("Welcome to the Task Manager CLI!")
    # Example usage for testing:
    # add_task(tasks, "Buy groceries")
    # print(tasks)
