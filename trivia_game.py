"""
Filename: trivia_game.py
Author: <Guardado, Gabriela>
Created: <09/11/2025>
Instructor: Holtslander
"""



print("Hello! Welcome to Trivia Game! In this Trivia game, you will have to answer the questions correctly to gain\n"
      "points. For every question you get correctly, you will gain +2 points. However, if you answer incorrectly then\n"
      "you will lose 2 points. There are a total of 10 questions. The questions you will be asked will be about\n "
      "different capitals from around the world. Good luck and have fun!\n")

score = 0
correct = 0

q1 = input("What is the capital of Virginia?\n").lower()
if q1 == "richmond":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 2
print("your points:\n", score)
print("Questions answered correct:\n", correct)
q2 = input("What is the capital of Wyoming?\n").lower()
if q2 == "cheyenne":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 2
print("your points:\n", score)
print("Questions answered correct:\n", correct)
q3 = input("What is the capital of Texas?\n").lower()
if q3 == "austin":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 2
print("your points:\n", score)
print("Questions answered correct:\n", correct)
q4 = input("What is the capital of Nara?\n").lower()
if q4 == "heijo-kyo":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 2
print("your points:\n", score)
print("Questions answered correct:\n", correct)
q5 = input("What is the capital of Italy?\n").lower()
if q5 == "rome":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 2
print("your points:\n", score)
print("Questions answered correct:\n", correct)
q6 = input("What is the capital of Spain?\n").lower()
if q6 == "madrid":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 2
print("your points:\n", score)
print("Questions answered correct:\n", correct)
q7 = input("What is the capital of Kenya?\n").lower()
if q7 == "nairobi":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 2
print("your points:\n", score)
print("Questions answered correct:\n", correct)
q8 = input("What is the capital of Japan?\n").lower()
if q8 == "tokyo":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 2
print("your points:\n", score)
print("Questions answered correct:\n", correct)
q9 = input("What is the capital of Argentina?\n").lower()
if q9 == "buenos aires":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 2
print("your points:\n", score)
print("Questions answered correct:\n", correct)
q10 = input("What is the capital of Brazil?\n").lower()
if q10 == "brasilia":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 2
print("your final score:\n", score)
print("Questions answered correct:\n", correct)

print("Thank you for using Trivia Game! I hope you enjoyed your experience!")