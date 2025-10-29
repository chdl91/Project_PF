import json

# Opening and Loading the POM.json and DIB.json files
POM_json = open("./Data/POM.json")
POM_data = json.load(POM_json)

DIB_json = open("./Data/DIB.json")
DIB_data = json.load(DIB_json)

# "Validate" Function to check the Quiz Answers if right or wrong.


def Validate():
    pass


# Closing the POM.json and DIB.json files
POM_json.close()
DIB_json.close()
