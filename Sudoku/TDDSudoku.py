import casosTest

toTest = casosTest.__dict__

def functForTDD(*toInput):
    toCorrect = toInput[0]
    functName = toInput[1]
    testName = toInput[2:]
    outputList = []

    for argument in testName:
        if argument in toTest.key():
            outputList.append(toTest[argument])
    outputList=tuple(outputList)
    print(functName(outputList) == toCorrect)
