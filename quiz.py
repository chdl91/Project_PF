import json
import random

# Opening and Loading the POM.json and DIB.json files
POM_json = open("./Data/POM.json")
POM_data = json.load(POM_json)

DIB_json = open("./Data/DIB.json")
DIB_data = json.load(DIB_json)


def POM_questions():
    num_questions = 10
    random_questions = random.sample(POM_data, num_questions)

# STOPPED HERE. CONTINUE WORK HERE (29.10.2025)


# "Validate" Function to check the Quiz Answers if right or wrong.
def validate():
    pass


# Closing the POM.json and DIB.json files
POM_json.close()
DIB_json.close()
