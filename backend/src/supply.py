import pandas as pd
import numpy as np
import datetime 

def createDF(csvs):
    attritionDf = pd.DataFrame(csvs["attrition"])
    populationDf = pd.DataFrame(csvs["population"])
    retirementDf = pd.DataFrame(csvs["retirement"]) 
    
    del attritionDf["rowID"]
    del populationDf["rowID"]
    del retirementDf["rowID"] 

    result = populationDf 

    def attrition(row):
        if row["Country of Personnel Area"] in attritionDf.columns:
            val = attritionDf.loc[attritionDf["Job Family"] == row["Job Family"]][row["Country of Personnel Area"]].values
            if val.empty:
                print(val)
                print(row)
        else:
            print(attritionDf.loc[attritionDf["Job Family"] == row["Job Family"]]["Others"])
            val = attritionDf.loc[attritionDf["Job Family"] == row["Job Family"]]["Others"]
        return val  
    
    result["Attrition"] = result.apply(attrition, axis=1)
 
    def retirement(row):
        dataframe = retirementDf.loc[retirementDf["Country of Personnel Area"] == row["Country of Personnel Area"]]
        if not(dataframe.empty):
            val = dataframe.values[0][1]  
        else:
            val =  retirementDf.loc[retirementDf["Country of Personnel Area"] == "Others"]
        return val
 
    result["Retirement"] = result.apply(retirement, axis=1)
    return result

def calculateSupply(csvs):
    df = createDF(csvs)
    print(df)
    year = datetime.datetime.now().date().year 
     
    duplicate = df[df.duplicated("Job title")] 
    print(duplicate) 
    return

