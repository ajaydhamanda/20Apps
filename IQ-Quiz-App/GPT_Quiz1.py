questions = [
    "What is the capital of France?",
    "What is the currency of Japan?",
    "What is the largest ocean in the world?",
    "What is the name of the world's longest river?"
    "What is the name of the highest mountain peak in the world?",
    "In which country is the Great Barrier Reef located?",
    "What is the name of the world's driest desert?",
    "What is the name of the world's tallest waterfall?",
    "What is the name of the world's biggest island?",
    "What is the name of the world's smallest country?",
    "What is the capital of Italy?",
    "What is the currency of the United States?",
    "What is the name of the largest lake in Africa?",
    "What is the name of the longest canyon in the world?",
    "What is the name of the highest peak in North America?",
    "What is the name of the largest desert in the world?",
    "What is the name of the tallest building in the world?",
    "In which country is the Eiffel Tower located?",
    "What is the name of the largest waterfall in the world?",
    "What is the name of the highest peak in Europe?"
]

answers = [
    "Paris",
    "Yen",
    "Pacific Ocean",
    "Nile",
    "Mount Everest",
    "Australia",
    "Atacama Desert",
    "Angel Falls",
    "Greenland",
    "Vatican City",
    "Rome",
    "Dollar",
    "Lake Victoria",
    "Grand Canyon",
    "Denali",
    "Antarctic Desert",
    "Burj Khalifa",
    "France",
    "Victoria Falls",
    "Mount Elbrus"
]

print("Welcome to my fist Demo Quiz!")

score = 0
for i in range(len(questions)):
    question = questions[i]
    answer = input(question + ": ")
    if answer.lower() == answers[i].lower():
        score += 1
        print("Correct!")
    else:
        print("No! The answer is", answers[i])

print("You got", score, "out of", len(questions), "questions correct.")
