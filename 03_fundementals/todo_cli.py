tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet")
    for i, task in enumerate(tasks, 1):
        print(f"{i}) {task}")

while True:
    cmd = input("Add, Show, Quit? ").strip().lower()
    if cmd == "add":
        task = input("What task: ")
        tasks.append(task)
    elif cmd == "show":
        show_tasks()
    elif cmd == "quit":
        break
