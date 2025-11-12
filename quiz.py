import json
import random

# Opening and Loading the POM.json and DIB.json files
POM_json = open("./Data/POM.json")
POM_data = json.load(POM_json)

DIB_json = open("./Data/DIB.json")
DIB_data = json.load(DIB_json)

while True:
    print("Welcome to the Quiz Application!")
    print("Menu")
    print("1. Principles of Management")
    print("2. Digital Business")
    print("3. Exit")
    input_choice = input(
        "Please select a subject by entering the corresponding number: ")
    if input_choice == '1':
        path = POM_data
        break
    if input_choice == '2':
        path = DIB_data
        break
    if input_choice == '3':
        exit()
    else:
        print("Bad Input. Please try again.")
        continue


def POM_questions():
    num_questions = 10
    random_questions = random.sample(POM_data, num_questions)


# Trying to print the Questions and Options from the POM.json file
# for random_questions in POM_questions():
   # print(f"Question: {"question"}")
    # print(f"Options: {"options"}")

while True:
    answer = input("Enter your answer (A, B, C, D): ")
    if answer in ['A', 'B', 'C', 'D']:
        break
    else:
        print("Invalid input. Please enter A, B, C, or D.")


# "Validate" Function to check the Quiz Answers if right or wrong.
def validate():
    pass


# Function to determine that if the Answer is correct then we add 1 point to the score.
# counter
def Counter():
    if validate() == True:
        score = + 1


# Closing the POM.json and DIB.json files
POM_json.close()
DIB_json.close()
