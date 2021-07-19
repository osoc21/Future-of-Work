import pandas as pd
import numpy as np
import datetime 

format = "%d.%m.%Y"

def createDF(csvs):
    attritionDf = pd.DataFrame(csvs["attrition"]) 
    populationDf = pd.DataFrame(csvs["population"])
    retirementDf = pd.DataFrame(csvs["retirement"])
    
    del attritionDf["rowID"]
    del populationDf["rowID"]
    del retirementDf["rowID"]
    
    populationDf["Birth date"] = pd.to_datetime(populationDf["Birth date"], format=format)

    result = populationDf

    def attrition(row):
        if row["Country of Personnel Area"] in attritionDf.columns:
            country = row["Country of Personnel Area"]
            jobFamily = row["Job Family"]
            val = attritionDf.loc[attritionDf["Job Family"] == jobFamily,country].values[0]
        else:
            val = attritionDf.loc[attritionDf["Job Family"] == row["Job Family"],"Others"].values[0]
        val = float(val.strip('%'))/100
        return val
     
    result["Attrition"] = result.apply(attrition, axis=1)

    def retirement(row): 
        dataframe = retirementDf.loc[retirementDf["Country of Personnel Area"] == row["Country of Personnel Area"]]
        retirementDate = row["Birth date"]
        if not(dataframe.empty):
            retirementDate = retirementDate.replace(year=retirementDate.year + int(dataframe.values[0][1]))
        else:
            retirementDate = retirementDate.replace(year=retirementDate.year + int(retirementDf.loc[retirementDf["Country of Personnel Area"] == "Others"].values[0][1]))
        return retirementDate
 
    result["Retirement"] = result.apply(retirement, axis=1)
    return result

def calculateSupply(csvs,horizon = 5):
    df = createDF(csvs)
    
    current = datetime.datetime.now() 
    
    unique = df.drop_duplicates(subset=["Job title"])

    resultDict = {}

    currentWF = df.loc[(df['Retirement'] > current)] 

    currentFTEs = {}

    #Calculate the current FTE of this year
    for title in unique["Job title"].values:
        currentWFTitle = currentWF.loc[currentWF["Job title"] == title]
        currentFTE = sum(list(map(float,currentWFTitle["FTE"].values)))
        currentFTEs[title] = currentFTE 
    resultDict[current.year] = currentFTEs

    def reduceAttrition(row):
        result = float(row["FTE"]) * (float(row["Attrition"].strip('%'))/100)
        return result

    #calculate the forcast for the coming years 
    forecast = currentFTEs.copy()
    for year in range(0,horizon):
        current = current.replace(year=current.year + 1)
        previous = forecast
        lastWF = currentWF
        currentWF = currentWF.loc[(df['Retirement'] > current)]
        for title in unique["Job title"].values:
            lastFTE = previous[title]
            retiringFTE = lastWF.loc[(df['Retirement'] <= current)].loc[lastWF["Job title"] == title]
            retiringFTE = sum(list(map(float,retiringFTE["FTE"].values)))
            resultFTE = lastFTE - retiringFTE
            if resultFTE < 0:
                print("smaller than 0")
            elif resultFTE == 0:
                print("zero")
            else:
                attritionFTE = currentWF.loc[currentWF["Job title"] == title]
                print(attritionFTE.apply(reduceAttrition,axis = 1))
            forecast[title] = resultFTE
 
        resultDict[current.year] = forecast.copy() 

    return

