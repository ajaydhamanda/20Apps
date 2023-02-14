'''
while True:
    user_action = input("Type add, show/display, edit, remove, complete or exit : ")
    user_action = user_action.strip()

    if 'add' in user_action:
       todo = user_action[4:]

    with open('todo.txt', 'r') as file:
            todos = file.readlines()

    todos.append(todo + '\n')

    with open('todo.txt', 'w') as file:
          file.writelines(todos)

    if  'show' or 'display' in user_action:

        with open('todo.txt', 'r') as file:
            todos = file.readlines()
        #new_todos = [item.strip(\n) for item in todos]
               new_todos = []
        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    if 'exit' in user_action:
        break

    if 'remove' in user_action:
        number = int(input("Enter the number of the item to remove: "))
        number -= 1
        rem_todo = todos.remove[number]
        print(rem_todo)

    if 'edit' in user_action:
        number = int(input("Enter the number of item you want to edit: "))
        number -= 1
        ed_todo = input("Enter the new to-do")
        todos[number] = ed_todo

    if 'complete' in user_action:
        number = int(input("Enter the number of the task completed"))
        number -= 1
        todos = todos.pop([number])
        print(todos)

'''

while True:
    user_action = input("Type add, show/display, edit, remove, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        print("Enter your new goal:")
        todo = input()

        with open('todo.txt', 'a') as file:
            file.write(todo + '\n')

        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            row = f"{index + 1}. {item.strip()}"
            print(row)

    if 'show' in user_action or 'display' in user_action:
        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        todos = [todo.strip() for todo in todos if todo.strip()]

        for index, item in enumerate(todos):
            element = f"{index + 1}. {item}"
            print(element)

    if 'exit' in user_action:
        with open('todo.txt', 'w') as file:
            file.writelines(todos)
        break

    if 'remove' in user_action:
        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        number = int(input("Enter the number of the item to remove: "))
        number -= 1
        todos.pop(number)

        with open('todo.txt', 'w') as file:
            file.writelines(todos)

        for index, item in enumerate(todos):
            element = f"{index + 1}. {item}"
            print(element)

    if 'edit' in user_action:
        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        number = int(input("Enter the number of item you want to edit: "))
        number -= 1
        ed_todo = input("Enter the new to-do: ")
        todos[number] = ed_todo + '\n'

        with open('todo.txt', 'w') as file:
            file.writelines(todos)

        for index, item in enumerate(todos):
            element = f"{index + 1}. {item}"
            print(element)

    if 'complete' in user_action:
        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        number = int(input("Enter the number of the task completed: "))
        number -= 1
        todos.pop(number)

        with open('todo.txt', 'w') as file:
            file.writelines(todos)

        for index, item in enumerate(todos):
            element = f"{index + 1}. {item}"
            print(element)

        print("Completed!")

