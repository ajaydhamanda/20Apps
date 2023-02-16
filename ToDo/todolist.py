todos = []

with open('todo.txt', 'r') as file:
    todos = [todo.strip() for todo in file.readlines() if todo.strip()]

def add_todo(todo):
    todos.append(todo)

def remove_todo(index):
    todos.pop(index)

def edit_todo(index, todo):
    todos[index] = todo

def complete_todo(index):
    todos.pop(index)

def save_todos():
    with open('todo.txt', 'w') as file:
        file.writelines('\n'.join(todos))

while True:
    user_action = input("Type add, show/display, edit, remove, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        print("Enter your new goal:")
        todo = input()

        add_todo(todo)

        for index, item in enumerate(todos):
            row = f"{index + 1}. {item.strip()}"
            print(row)

    if 'show' in user_action or 'display' in user_action:
        for index, item in enumerate(todos):
            element = f"{index + 1}. {item}"
            print(element)

    if 'exit' in user_action:
        save_todos()
        break

    if 'remove' in user_action:
        number = int(input("Enter the number of the item to remove: "))
        number -= 1

        remove_todo(number)

        for index, item in enumerate(todos):
            element = f"{index + 1}. {item}"
            print(element)

    if 'edit' in user_action:
        number = int(input("Enter the number of item you want to edit: "))
        number -= 1

        todo = input(f"Enter the new to-do (current: {todos[number]}): ")

        edit_todo(number, todo)

        for index, item in enumerate(todos):
            element = f"{index + 1}. {item}"
            print(element)

    if 'complete' in user_action:
        number = int(input("Enter the number of the task completed: "))
        number -= 1

        complete_todo(number)

        for index, item in enumerate(todos):
            element = f"{index + 1}. {item}"
            print(element)

        print("Completed!")
