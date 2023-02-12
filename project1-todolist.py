
user_prompt = "Type enter add, show or exit : "
todos = []
while True:
    action = input(user_prompt)
    action = action.strip()

    match action:
        case 'add':
            todo = input("Enter an item to add to your to do list: ")
            todos.append(todo)
            print(todos)
        case  'show':
            for item in todos:
                print(todos)
        case 'exit':
            break


print("Here is your to-do list! Do visit again.")



