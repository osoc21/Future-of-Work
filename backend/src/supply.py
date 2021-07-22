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
    populationDf["FTE"] = pd.to_numeric(populationDf["FTE"])

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

def calculateSupplyTitle(csvs,horizon = 5):
    currentWF = createDF(csvs)
    
    current = datetime.datetime.now() 

    uniqueFamily = currentWF.drop_duplicates(subset=["Job Family"])["Job Family"].values
    
    familyDict = {}

    for family in uniqueFamily:
        jobs = currentWF.loc[(currentWF["Job Family"] == family)].drop_duplicates(subset=["Job title"])["Job title"].values
        familyDict[family] = jobs

    result = []

    #calculate the forcast for the coming years
    for _ in range(0,horizon):
        forecast = {}
        currentWF = currentWF.loc[(currentWF['Retirement'] > current)]
        for family in familyDict:
            currentWFFamily = currentWF.loc[currentWF["Job Family"] == family]
            titles = []
            for title in familyDict[family]:
                currentWFTitle = currentWFFamily.loc[currentWF["Job title"] == title]
                currentFTE = sum(list(map(float,currentWFTitle["FTE"].values)))
                titles.append({title:currentFTE})
            forecast[family] = titles  
        result.append({"year":current.year,"data":forecast})
        currentWF["FTE"] = currentWF["FTE"] * (1 - currentWF["Attrition"])
        current = current.replace(year=current.year + 1)
    return result

