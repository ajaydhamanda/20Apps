'''

while True:
    greeting = input("Hello, what is your name?")
    print(greeting.upper() '''

'''
countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country.capitalize())
    print(countries)

'''
'''
meals = ['chocolate', 'noodles', 'salad']
    for meals in meals:
    print (meal.capitalize())'''

'''names = ["john smith", "sen plakay", "dora ngacely"]

for items in names:
    print(items.title())
''''''
items = ['raw food', 'raw meat', 'raw fish']
for item in items:
    item = item.replace('raw', 'No.')
    print(item)
'''
'''
elements = ['a', 'b', 'c']
new = 'x'
elements[1] = new
print(elements)
'''
'''
waiting_list = ['Abc', 'Gedf', 'Hname3', 'ZnZame4', 'name']
waiting_list.sort()
for index, item in enumerate(waiting_list):
    row = f"{index}.{item.capitalize()}"
    print(row)
    
'''
'''zz
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