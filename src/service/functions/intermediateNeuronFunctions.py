import math

def getOutput(inputs: list):
    inputSum = sum(inputs)
    return math.tanh(inputSum)
