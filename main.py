# main.py
def add_task(task_list, task_description):
    task_list.append(task_description)
    print(f"Task '{task_description}' added.")

def show_tasks(task_list):
    if not task_list:
        print("No tasks to show.")
        return
    print("Your tasks:")
    for i, task in enumerate(task_list):
        print(f"{i + 1}. {task}")

def delete_task(task_list, task_index):
    if 0 <= task_index < len(task_list):
        deleted_task = task_list.pop(task_index)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    tasks = ["Finish assignment", "Call mom"] # Sample tasks
    print("Welcome to the Task Manager CLI!")
    # Example usage for testing:
    # delete_task(tasks, 0) # Deletes "Finish assignment"
    # show_tasks(tasks)
