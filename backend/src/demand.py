import pandas as pd
import datetime 
import math

# A list of all operators
operators = {"*","+","**","-","log"}
# Custom lambdas for functions not defined in python
myOperators = {"log":lambda x,y: math.log(x,y)}

def createDF(csv):
    '''Create a dataframe for the demand'''
    # create the data frame
    demandDF = pd.DataFrame(csv["demand"])
    # remove the row ID
    del demandDF["rowID"]
    return demandDF

def extractInfoFormulas(formulas):
    '''Extract the info from the formulas'''
    # A set for the parameters, operators and coefficients
    parameterSet = set()
    operatorSet = set()
    coefficientSet = set()
    # Go over each formula
    for formula in formulas:
        # Go over each string
        for string in formula.split():
            # Look whether the string is in the operators
            if string in operators:
                operatorSet.add(string)
            # Look whether the string is a float or numeric
            elif string.replace('.', '', 1).isdigit():
                coefficientSet.add(string)
            # Add it to the parameters otherwise
            else:
                parameterSet.add(string)
    return {
        "parameters":parameterSet,
        "operators":operatorSet,
        "coefficients":coefficientSet
        }

def getFormulas(csv):
    '''Get all the formulas from the csvs'''
    # Create the demand dataframe
    demandDF = createDF(csv)
    # Get the formulas as a list
    return demandDF["Formula"].tolist()

def calculateFormula(formula,values):
    '''Calculate the result of a certain formula'''
    # Make a float for each value in the values
    values = {k : float(v) for k,v in values.items()}
    # Create the variables by adding the operators
    variables = {**values,**myOperators}
    # Eval the formula
    return eval(formula,values) 

def calculateDemand(csv,parameters,familyDict):
    '''Calculate the demand result'''
    # Create the demand dataframe
    demandDF = createDF(csv)
    parameterDF = pd.DataFrame(parameters)

    result = [] 
    # We get the years for which we want to calculate the demand
    years = list(parameterDF)  
    years.remove('parameter')
    # We go over each year and calculate the FTE for each family
    for year in years:
        forecast = {}
        parameter = {}
        for _,row in parameterDF[[year,'parameter']].iterrows():
            parameter[row['parameter']] = row[year]
        # We go over each family
        for family in familyDict:
            titles = []
            # We go over each job
            for title in familyDict[family]:
                jobs = demandDF.loc[demandDF["Job title"]==title]
                # If we can't find the job in the profiles we just add a 0 this can be changed to be the FTE in the current year
                if jobs.empty:
                    titles.append({title:0})
                else:
                    formula = jobs["Formula"].values[0]
                    titles.append({title: calculateFormula(formula,parameter)})
            forecast[family] = titles
        result.append({"year":year,"data":forecast})
    return result
