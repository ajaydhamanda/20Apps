
user_prompt = "Type add, show/display, edit, remove or exit : "
todos = []
while True:
    action = input(user_prompt)
    action = action.strip()

    match action:
        case 'add':
            todo = input("Enter an item to add to your to do list: ")
            todos.append(todo)
            print(todos)
        case  'show' | 'display':
            for item in todos:
                item = item.capitalize()
                print(item)
        case 'exit':
            break
        case 'remove':
            number = int(input("Enter the number of the item to remove: "))
            number -= 1
            rem_todo = todos.remove(todos[number])
            print(rem_todo)
        case 'edit':
            number = int(input("Enter the number of item you want to edit: "))
            number -= 1
            ed_todo = input("Enter the new to-do")
            todos[number] = ed_todo
        case unrecognized:
            print("Sorry, please try again. Type add, show or exit: ")
print("Here is your to-do list! Do visit again.")




