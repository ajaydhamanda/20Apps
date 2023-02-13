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