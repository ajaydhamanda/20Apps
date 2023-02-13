

questions = [
            "What is the capital of France?",
            "Who was the first president of the US?",
            "Who painted the Mona Lisa?",
            "Who wrote the novel \"To Kill a Mockingbird?\"",
            "Who composed Beethoven's 5th Symphony?",
            "What is the largest ocean on Earth?",
            "Who discovered penicillin?",
            "Who is the current Queen of England?",
            "What is the currency of Japan?",
            "What is the name of the first man on the moon?",
    ]
answers = [
    ("A. London/B. Paris/C. Rome/D. Madrid"),
    ("A. George Washington/B. John Adams/C. Thomas Jefferson/D. Abraham Lincoln"),
    ("A. Michelangelo/B. Leonardo da Vinci/C. Raphael/D. Rembrandt"),
    ("A. Harper Lee/B. Mark Twain/C. Ernest Hemingway/D. F. Scott Fitzgerald"),
    ("A. Mozart/B. Beethoven/C. Brahms/D. Tchaikovsky"),
    ("A. Pacific/B. Atlantic/C. Indian/D. Arctic"),
    ("A. Louis Pasteur/B. Alexander Fleming/C. Charles Darwin/D. Robert Koch"),
    ("A. Elizabeth I/B. Elizabeth II/C. Victoria/D. Mary"),
    ("A. Elizabeth I/B. Elizabeth II/C. Victoria/D. Mary"),
    ("A. Neil Armstrong/B. Buzz Aldrin/C. Yuri Gagarin/D. John Glenn"),
       ]

       correct_answer =["C", "D", "B", "F", "F", "C", "B", "C", "C", "C"]]


def test_check(score):
    score = 0
    question = question[0]
    correct_answer = answer[0]
    answer = input(str(question))
    if answer == correct_answer:
        score += 1
    return (score)

print(score)
    
