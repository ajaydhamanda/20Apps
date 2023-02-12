user_prompt = "Enter an element to add to your to-do list:"

todos = []

while True:
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo)
    print(todos)



