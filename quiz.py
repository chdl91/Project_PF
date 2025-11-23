import json
import random
import signal

# Opening and Loading the POM.json and DIB.json files
POM_json = open("./Data/POM.json")
POM_data = json.load(POM_json)

DIB_json = open("./Data/DIB.json")
DIB_data = json.load(DIB_json)


def run_quiz(data, per_question_timer=60):
    """Run a quiz session on the provided data. Type 'menu' to return to the main menu."""
    if not isinstance(data, list) or len(data) == 0:
        print("No questions available.")
        return


signal.signal(signal.SIGALRM, _timeout_handler)

num_questions = min(10, len(data))
questions = random.sample(data, num_questions)

for q in questions:
    print(f"\nQuestion: {q.get('question', '<no question>')}\n")
    print(f"Answers: {q.get('answers', q.get('options', '<no answers>'))}")

     while True:
          answer = input(
               "Enter your answer (1, 2, 3, 4) or type 'menu' to return to menu: ").strip()
           if answer.lower() == 'menu':
                print("Returning to menu...")
                return  # return to the caller (the menu loop)
            if answer in ['1', '2', '3', '4']:
                break
            print("Invalid input. Please enter 1, 2, 3, 4, or 'menu'.")


while True:
    print("\nWelcome to the Quiz Application!")
    print("Please select a subject:")
    print("1. Principles of Management")
    print("2. Digital Business")
    print("3. Exit")
    input_choice = input(
        "Please select a subject by entering the corresponding number: ").strip()

    if input_choice == '1':
        run_quiz(POM_data)
        # returns here when user types 'menu' during run_quiz
    elif input_choice == '2':
        run_quiz(DIB_data)
    elif input_choice == '3':
        print("Goodbye.")
        break
    else:
        print("Bad Input. Please try again.")
        continue

# Closing the POM.json and DIB.json files
POM_json.close()
DIB_json.close()
