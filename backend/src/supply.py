import pandas as pd
import datetime 

format = "%d.%m.%Y"

def createDF(csvs):
    '''Create the data frames for the data frames'''
    # create a pandas dataframe for each of the supply csvs
    attritionDf = pd.DataFrame(csvs["attrition"]) 
    populationDf = pd.DataFrame(csvs["population"])
    retirementDf = pd.DataFrame(csvs["retirement"])
    # delete the rowIDs
    del attritionDf["rowID"]
    del populationDf["rowID"]
    del retirementDf["rowID"]
    # Change the birth date to be of the type datetime and FTE to the nemeric type   
    populationDf["Birth date"] = pd.to_datetime(populationDf["Birth date"], format=format)
    populationDf["FTE"] = pd.to_numeric(populationDf["FTE"])

    result = populationDf
    # create a float value from the attrition rate from the result
    def attrition(row):
        if row["Country of Personnel Area"] in attritionDf.columns:
            country = row["Country of Personnel Area"]
            jobFamily = row["Job Family"]
            val = attritionDf.loc[attritionDf["Job Family"] == jobFamily,country].values[0]
        else:
            val = attritionDf.loc[attritionDf["Job Family"] == row["Job Family"],"Others"].values[0]
        val = float(val.strip('%'))/100
        return val
    # We create a column on the result dataframe
    result["Attrition"] = result.apply(attrition, axis=1)
    # We calculate the retirement date from the population and retirement age 
    def retirement(row): 
        dataframe = retirementDf.loc[retirementDf["Country of Personnel Area"] == row["Country of Personnel Area"]]
        retirementDate = row["Birth date"]
        if not(dataframe.empty):
            retirementDate = retirementDate.replace(year=retirementDate.year + int(dataframe.values[0][1]))
        else:
            retirementDate = retirementDate.replace(year=retirementDate.year + int(retirementDf.loc[retirementDf["Country of Personnel Area"] == "Others"].values[0][1]))
        return retirementDate
    # We create a column for the retirement date from each
    result["Retirement"] = result.apply(retirement, axis=1)
    return result

def calculateSupplyTitle(csvs,horizon = 5):
    '''Calculate the supply result'''
    # We create a dataframe from the csvs
    currentWF = createDF(csvs)
    # We get the current date
    current = datetime.datetime.now() 
    # We get the unique job families
    uniqueFamily = currentWF.drop_duplicates(subset=["Job Family"])["Job Family"].values
    familyDict = {}
    # We get each job in each family
    for family in uniqueFamily:
        jobs = currentWF.loc[(currentWF["Job Family"] == family)].drop_duplicates(subset=["Job title"])["Job title"].values
        familyDict[family] = jobs

    result = []

    #calculate the forcast for the coming years
    # we go over each year
    for _ in range(0,horizon):
        forecast = {}
        # We remove all the employees who will retire on the year in current
        currentWF = currentWF.loc[(currentWF['Retirement'] > current)]
        # We go over each family
        for family in familyDict:
            currentWFFamily = currentWF.loc[currentWF["Job Family"] == family]
            titles = []
            # We go over each job title in the family
            for title in familyDict[family]:
                currentWFTitle = currentWFFamily.loc[currentWF["Job title"] == title]
                currentFTE = sum(list(map(float,currentWFTitle["FTE"].values)))
                titles.append({title:currentFTE})
            # We put the result in the forecast
            forecast[family] = titles  
        # We the forecast in the result
        result.append({"year":current.year,"data":forecast})
        # We update the FTE for everyone
        currentWF["FTE"] = currentWF["FTE"] * (1 - currentWF["Attrition"])
        # We update our current year to the next year
        current = current.replace(year=current.year + 1)
    return result

def jobFamilyTitle(csvs):
    '''Get the jobs for each family'''
    # create the data frame
    currentWF = createDF(csvs) 
    # get the unique family names
    uniqueFamily = currentWF.drop_duplicates(subset=["Job Family"])["Job Family"].values
    
    familyDict = {}
    # We go over each family
    for family in uniqueFamily:
        jobs = currentWF.loc[(currentWF["Job Family"] == family)].drop_duplicates(subset=["Job title"])["Job title"].values
        # We store the job under the family
        familyDict[family] = jobs
    return familyDict