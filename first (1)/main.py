tasks = []


def addTask():
  task = input("please enter a task")
  tasks.append(task)
  print(f"Task {task} added successfully into the list")


def listTasks():
  if not tasks:
    print("There are no tasks currently.")
  else:
    print("current tasks:")
    for index, task in enumerate(tasks):
      print(f"Task #{index}. {task} ")

def editTask():
  listTasks()
  task_index = int(input("Enter the task number to edit: "))
  if 0 <= task_index < len(tasks):
    new_task = input("Enter the new task: ")
    tasks[task_index] = new_task
    print("Task edited successfully.")
  else:
    print("Invalid task number.")

def deleteTask():
  listTasks()

  try:
    taskToDelete = int(input("Enter the # to   delete: "))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task (taskToDelete) has been removed.")

    else:

      print(f"Task #{taskToDelete} was not found.")

  except:

    print("Invalid input.")


if __name__ == "__main__":
  print("welcome to the to do list :)")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Edit List")
    print("4. List all tasks")
    print("5. Quit")

    choice = input("Enter your choice: ")
    if (choice == "1"):
      addTask()
    elif (choice == "2"):
      deleteTask()
    elif (choice == "3"):
      editTask()
    elif (choice == "4"):
      listTasks()
    elif (choice == "5"):
      print("Thank you for using the to do list")
      break
    else:
      print("Invalid choice. Please try again.")

print("thank you for using the to do list")
