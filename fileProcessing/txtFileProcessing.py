import re

## Start of Functions ============================================
def readFile(filePath: str):
    with open(filePath, "r", encoding="utf-8") as f:
        return f.readlines()
    
def processFile(file: list):
    return [word[:len(word)-1] for word in file]

def calcCountofEachWord(file: list):
    d = {
        "O": 0,
        "B-positive": 0,
        "B-negative": 0,
        "B-neutral": 0,
        "I-positive": 0,
        "I-negative": 0,
        "I-neutral": 0
    }
    for i in range(len(file)):
        if file[i] != "":
            l = file[i].split()
            entity = l[0]
            label = l[1]
            key = f"{entity}_{label}"
            if key in d:
                d[key] += 1
                d[label] += 1
            else:
                d[key] = 1
                d[label] += 1
    return d

def calcEmission(input_d: dict):
    emissionResult = 1
    output_d = {}
    label_l = ["O", "B-positive", "B-negative", "B-neutral", "I-positive", "I-negative", "I-neutral"]
    # print(input_d["O"], input_d["B-positive"], input_d["B-negative"])
    for key, value in input_d.items():
        if key not in label_l:
            label = key.split("_")[1]
            val = value / input_d[label]
            # print(f"Curr value: {val}")
            output_d[key] = val
            emissionResult *= val
    return emissionResult, output_d
    pass
## End of Functions ============================================

### Init variables
filePath = "../Data/ES/train"

## Calling Functions
rawFile = readFile(filePath)
processedFile = processFile(rawFile)[0:50]

testFile = processedFile

d = calcCountofEachWord(testFile)
emissionResult, d1 = calcEmission(d)
print(d1)
print(emissionResult)
