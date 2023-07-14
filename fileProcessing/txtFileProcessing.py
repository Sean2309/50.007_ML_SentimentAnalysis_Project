import re

## Functions
def readFile(filePath: str):
    with open(filePath, "r", encoding="utf-8") as f:
        return f.readlines()
    
def processFile(file: list):
    return [word[:len(word)-1] for word in file]

def calcCountofEachWord(file: list):
    d = {}
    label_l = ["B-positive", "B-negative", "O"]
    d["countY"] = 0
    for i in range(len(file)):
        if file[i] != "":
            l = file[i].split()
            entity = l[0]
            label = l[1]
            
            key = f"{entity}_{label}"
            if key in d:
                d[key] += 1
            else:
                d[key] = 1
            if label in label_l:
                d["countY"] += 1
    return d

def calcEmission(input_d: dict):
    countY = input_d["countY"]
    emissionResult = 1
    for key, value in input_d.items():
        if key != "countY":
            val = value / countY
            emissionResult *= val
    return emissionResult
    pass


### Init variables
filePath = "../Data/ES/train"

## Calling Functions
rawFile = readFile(filePath)
processedFile = processFile(rawFile)

testFile = processedFile[0:100]

d = calcCountofEachWord(testFile)
emissionResult = calcEmission(d)
print(emissionResult)