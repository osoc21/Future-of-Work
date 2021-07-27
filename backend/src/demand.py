import pandas as pd
import datetime 
import math

operators = {"*","+","**","-","log"}

myOperators = {"log":lambda x,y: math.log(x,y)}

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
    variables = {**values,**myOperators}
    return eval(formula,values) 

def calculateDemand(csv,parameters,familyDict):
    demandDF = createDF(csv)
    parameterDF = pd.DataFrame(parameters)
    
    result = [] 
    years = list(parameterDF)  
    years.remove('parameter')
    for year in years:
        forecast = {}
        parameter = {}
        for _,row in parameterDF[[year,'parameter']].iterrows():
            parameter[row['parameter']] = row[year]
        for family in familyDict:
            titles = []
            for title in familyDict[family]:
                jobs = demandDF.loc[demandDF["Job title"]==title]
                if jobs.empty:
                    titles.append({title:0})
                else:
                    formula = jobs["Formula"].values[0]
                    titles.append({title: calculateFormula(formula,parameter)})
            forecast[family] = titles
        result.append({"year":year,"data":forecast})

    return result
