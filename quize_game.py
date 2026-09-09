#list of questions
score = 10
import random


questions = ["What is the capital city of Kenya?",
             "What is the capital city of Tanzania?",
             "how many days are there in a week?",
             "What colour is the sky?"]

choices = [{"A": "Mombasa", "B": "Nairobi", "C": "Kisumu", "D": "Nakuru"},
           {"A": "Dodoma", "B": "Dar es Salaam", "C": "Mwanza", "D": "Arusha"},
           {"A": "5", "B": "6", "C": "7", "D": "8"},
           {"A": "Blue", "B": "Green", "C": "Red", "D": "Yellow"}]
 
answers = ["B", "A", "C", "A"]

# create a list of indexes to keep track of the questions

indexes = list(range(len(questions)))
random.shuffle(indexes)
#loop for using the randomised indexes to ask the questions
for i in indexes:
    print(questions[i])
    for key, value in choices[i].items():
        print(f"{key}: {value}")
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    if user_answer == answers[i]:
        score += 10
        print("Correct!")
    else:
        print("Incorrect!")

