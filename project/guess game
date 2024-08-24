import random

from questions import *

print("Welcome to the Quiz Game")

game_on = True

playing = input("Do you want to test your knowledge?Type 'yes'/'no': ")
if playing != 'yes':
    game_on = False

points = 0
lives = 5

while game_on:
    # getting hold of a question from the dictionary
    question = random.choice(list(general_knowledge.keys()))

    # asking user the answer
    user_input = input(f"{question}: ")
    if user_input == general_knowledge[question].lower():
        print("Correct answer :)")
        points += 1
        print(f"Current Score: {points}")
    else:
        print("WRONG ANSWER!! LOST 1 CHANCE")
        lives -= 1
        print(f"Current chances: {lives}")

    if lives == 0:
        print(f"YOUR TOTAL SCORE --> {points}")
        game_on = False

