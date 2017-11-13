import re
def main():
    Weights =[]
    tophalf = []
    #DATA MUST BE MANUALLY APPENDED INTO ARRAYS IN ORDER TO TEST THIS COMPONENT





def ComputeFormula(Weights, tophalf):
    Overallweight = sum(Weights)
    overalltop = sum(tophalf)
    answer = overalltop / Overallweight
    print(answer)
    return answer