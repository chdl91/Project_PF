import json
import random
import signal

# Opening and Loading the POM.json and DIB.json files
POM_json = open("./Data/POM.json")
POM_data = json.load(POM_json)

DIB_json = open("./Data/DIB.json")
DIB_data = json.load(DIB_json)

# This function handles the timeout for each question
def _timeout_handler(signum, frame): 
    raise TimeoutError("Time is up")
signal.signal(signal.SIGALRM, _timeout_handler)


def run_quiz(data, per_question_timer=60):
    """Run a quiz session on the provided data. Type 'menu' to return to the main menu."""
    if not isinstance(data, list) or len(data) == 0:
        print("No questions available.")
        return
    
    num_questions = min(10, len(data))
    questions = random.sample(data, num_questions)
    collected_answers = []
    for q in questions:
        print(f"\nQuestion: {q.get('question', '<no question>')}\n")
        answers = q.get('answers', q.get('options', []))
        # Normalize answers into a list so we can print them line by line
        if isinstance(answers, dict):
            answers_list = list(answers.values())
        else:
            answers_list = answers

        if isinstance(answers_list, list):
            print("Answers:")
            for idx, opt in enumerate(answers_list, start=1):
                print(f"  {idx}. {opt}")
        else:
            print(f"Answers: {answers_list}")
        # For each question: wait for user input before continuing
        while True:
            try:
                signal.alarm(per_question_timer)  # Set the alarm
                answer = input(
                    f"Enter your answer (1, 2, 3, 4) or type 'menu' to return to menu [{per_question_timer}s]: "
                ).strip()
            except TimeoutError:
                print("\nTime's up! Moving to the next question.")
                collected_answers.append(None)  # Record no answer
                break  # Move to the next question on timeout
            finally:
                # Ensure alarm is always disabled after input/timeout
                try:
                    signal.alarm(0)
                except Exception:
                    pass

            if answer.lower() == 'menu':
                print("Returning to menu...")
                return

            if answer in ['1', '2', '3', '4']:
                collected_answers.append(answer)
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
