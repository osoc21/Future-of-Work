import pandas as pd

operators = {"*","+","**","-"}

def createDF(csv):
    demandDF = pd.DataFrame(csv["demand"])

    del demandDF["rowID"]

    return demandDF

def extractInfoFormulas(formulas):
    parameterSet = set()
    operatorSet = set()
    coefficientSet = set()
    for formula in formulas:
        for string in formula.split():
            if string in operators:
                operatorSet.add(string)
            elif string.replace('.', '', 1).isdigit():
                coefficientSet.add(string)
            else:
                parameterSet.add(string)
    return {
        "parameters":parameterSet,
        "operators":operatorSet,
        "coefficients":coefficientSet
        }

def getFormulas(csv):
    demandDF = createDF(csv)

    return demandDF["Formula"].tolist()

def calculateDemand(formula,values):
    values = {k : float(v) for k,v in values.items()}
    variables = values
    return eval(formula,variables)