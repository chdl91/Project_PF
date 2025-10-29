import json

POM_json = open("./Data/POM.json")
POM_data = json.load(POM_json)

DIB_json = open("./Data/DIB.json")
DIB_data = json.load(DIB_json)

POM_json.close()
DIB_json.close()
