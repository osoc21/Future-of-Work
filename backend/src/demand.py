import pandas as pd
import datetime 

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

def calculateFormula(formula,values):
    values = {k : float(v) for k,v in values.items()}
    variables = values
    return eval(formula,variables)

def calculateDemand(csv,parameters,familyDict):
    demandDF = createDF(csv)

    current = datetime.datetime.now() 

    result = []

    for year in range(0,len(list(parameters)[0]) - 1):
        forecast = {}
        parameter = {k: v[year] for k, v in parameters.items()}
        for family in familyDict:
            titles = []
            for title in familyDict[family]:
                jobs = demandDF.loc[demandDF["Profile"]==title]
                if jobs:
                    titles.append({title: calculateFormula(jobs[0],parameter)})
                else:
                    titles.append({title:0})
        result.append({"year":current.year,"data":forecast})
        current = current.replace(year=current.year + 1)
    
    return result