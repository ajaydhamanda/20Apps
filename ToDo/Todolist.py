user_prompt = "Type add, show/display, edit, remove, complete or exit : "
while True:
    action = input(user_prompt)
    action = action.strip()

    match action:
        case 'add':
            todo = input("Enter an item to add to your list: ") + "\n"

            file = open('todo.txt', 'r')     #fix code here
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todo.txt', 'w')
            file.writelines(todos)
            file.close()
            print("Added!")
        case  'show' | 'display':           #fix code here
            file = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(todos)
        case 'exit':
            break
        case 'remove':
            number = int(input("Enter the number of the item to remove: ")) #fix code here
            number -= 1
            rem_todo = todos.remove(todos[number])
            print(rem_todo)
        case 'edit':
            number = int(input("Enter the number of item you want to edit: "))
            number -= 1
            ed_todo = input("Enter the new to-do")
            todos[number] = ed_todo
        case 'complete':
            number = int(input("Enter the number of the task completed"))
            number -= 1
            todos = todos.pop(number)
            print(todos)
        case unrecognized:
            print("Sorry, please try again. Type add, show or exit: ")
