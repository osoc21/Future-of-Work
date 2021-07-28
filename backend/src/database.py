from uuid import uuid1
import csv
import io
import json 
import datetime

def writeCSVs(supplyFiles,supplyNames,demandFile,redis):
    '''Writes all of the csv files being population, attrition, retirement and the demand file to the redis database'''
    # We generate a unique ID for a global
    globalID = str(uuid1())
    supplyID = str(uuid1())
    demandID = str(uuid1())
    # Supply mapping #
    # Here we go over each file in the supplyFiles and we put it onto our Redis store
    filesIDs = {}
    for file,name in zip(supplyFiles,supplyNames):
        ids = []
        dataID = str(uuid1())
        # We open the csv file to store it row per row so that we can access it later when other requests are made
        with io.TextIOWrapper(file, encoding='utf-8') as text_file:
            csvReader = csv.DictReader(text_file, delimiter=',')
            for row in csvReader:
                id = str(uuid1())
                ids.append(id)
                redis.set(id,str(row))
        # Set the data id to the list of all the IDs containing the rows
        redis.set(dataID,str(ids))
        filesIDs[name] = {'id':dataID}
    # We store the whole supply side under the supply ID
    redis.set(supplyID,str(filesIDs))
    # Demand mapping #
    # We make a unique id for the demandFile
    demandFileID = str(uuid1())
    demandIds = []
    # We open the demandFile to store it row per row so that we can access it later when other requests are made
    with io.TextIOWrapper(demandFile, encoding='utf-8') as demand_text_file:
        demandCSVReader = csv.DictReader(demand_text_file, delimiter=',')
        for demandRow in demandCSVReader: 
            id = str(uuid1())
            demandIds.append(id)
            redis.set(id,str(demandRow))
        # Set the demand file id to the list of IDs containing the rows
        redis.set(demandFileID,str(demandIds))
    # We store the whole demand side under the demand ID
    redis.set(demandID,str({"csv":demandFileID,"parameters":str(uuid1())}))
    # Global mapping #
    # We store the demandID and supplyID under the global ID
    redis.set(globalID,str({"supply":supplyID,"demand":demandID}))
    return globalID 

def readCSVs(id,redis):
    '''Reads all the data from the redis database which are population, attrition, retirement and the demand file'''
    # We get the demand and supply ID from the redis datastore
    globalDict = eval(redis.get(str(id)).decode())
    # supply loading
    # We get all the file IDs from the datastore
    filesIDs = eval(redis.get(globalDict["supply"]).decode()) 
    result = {}
    # We go over each of the files and read in all the rows and make them into a JSON formatteData
    # Note: here the JSON result contains the rowID so that we could change them in the frontend (This functionality is not implemented yet)
    for fileName in filesIDs:
        fileID = filesIDs[fileName]
        rowIDS = eval(redis.get(fileID['id']).decode())
        rows = []
        # We go over each row and add them to the rows list
        for rowID in rowIDS:
            row = eval(redis.get(rowID))
            row["rowID"] = rowID
            rows.append(row)
        # We add the rows to the result under the filename
        result[fileName] = rows
    # demand loading
    # We get the ID of the demandfile
    demandFileID = eval(redis.get(globalDict["demand"]).decode())["csv"]
    demandRowIDs = eval(redis.get(demandFileID))
    rows = []
    # We go over each row and add them to the rows list
    # Note: here the JSON result also contains the rowID so that we could change them in the frontend (This functionality is not yet implemented)
    for rowID in demandRowIDs:
        row = eval(redis.get(rowID))
        row["rowID"] = rowID
        rows.append(row)
    # We add the rows to the result under the name demand
    result["demand"] = rows
    return result

def writeSupplyCSVs(files,names,redis):
    '''Write all the supply csvs to the redis database'''
    # We create a global ID
    globalID = str(uuid1())

    filesIDs = {}
    # We go over each file and name to create the redis id and store the rows
    for file,name in zip(files,names):
        ids = []
        dataID = str(uuid1())
        # Here we open the file and read each row
        with io.TextIOWrapper(file, encoding='utf-8') as text_file:
            csvReader = csv.DictReader(text_file, delimiter=',')
            for row in csvReader:
                id = str(uuid1())
                ids.append(id)
                redis.set(id,str(row))
        # We set the dataID to the ids under which we stored the rows
        redis.set(dataID,str(ids))
        filesIDs[name] = {'id':dataID}
    # We create a supply ID and a demand ID and store it on the redis database as well
    supplyID = str(uuid1())
    redis.set(globalID,str({"supply":supplyID,"demand":str(uuid1())}))
    redis.set(supplyID,str(filesIDs))
    return globalID
 
def readSupplyCSVs(id,redis):
    '''Read the supply data from the redis database'''
    # We get the supplyID from the redis database
    globalDict = eval(redis.get(str(id)).decode())
    # We get the filesID from the redis database
    filesIDs = eval(redis.get(globalDict["supply"]).decode()) 
    result = {}
    # We go over the files and get the rows
    for fileName in filesIDs:
        fileID = filesIDs[fileName]
        rowIDS = eval(redis.get(fileID['id']).decode())
        rows = []
        # We go over each row and add them to the rows list
        for rowID in rowIDS:
            row = eval(redis.get(rowID))
            row["rowID"] = rowID
            rows.append(row)
        # We add the rows to the result under the fileName
        result[fileName] = rows
    return result

def writeDemandCSV(globalID,file,redis):
    '''Write the demand file to the redis database'''
    # We get the demand file from the redis database
    globalDict = eval(redis.get(str(globalID)).decode())
    demandID = globalDict["demand"]
    ids = []
    # We go over the demand file and write each row to the redis database
    with io.TextIOWrapper(file, encoding='utf-8') as text_file:
        csvReader = csv.DictReader(text_file, delimiter=',')
        # We go over each rows and put them on the redis database
        for row in csvReader:
            id = str(uuid1())
            ids.append(id)
            redis.set(id,str(row))
    # We put the rows on the redis database under the demand ID
    redis.set(demandID,str(ids))

def readDemandCSV(globalID,redis):
    '''Read the demand file from the redis database'''
    # We get the demand file from the redis database
    globalDict = eval(redis.get(str(globalID)).decode())
    # We get the demand file ID
    demandFileID = eval(redis.get(globalDict["demand"]).decode())["csv"]
    demandRowIDs = eval(redis.get(demandFileID))
    rows = [] 
    # We go over each row and add them to the rows list
    for rowID in demandRowIDs:
        row = eval(redis.get(rowID)) 
        row["rowID"] = rowID
        rows.append(row)
    return {"demand":rows}

def writeDemandParameter(globalID,parameters,default,redis,horizon = 5):
    '''Write the demand parameters and instantiate them'''
    # We get the globalDict to look for the demand
    globalDict = eval(redis.get(str(globalID)).decode())
    # We get the parameters ID 
    demandParameterID = eval(redis.get(globalDict["demand"]).decode())["parameters"]
    # We instantiate the result list
    result = []
    # we go over each parameter in the parameters list
    for parameter in parameters:
        current = datetime.datetime.now() 
        years = []    
        parameterID = str(uuid1())
        # We go over the horizon of the years
        for _ in range(0,horizon):
            redis.set(parameterID + str(current.year),str(default))
            years.append(current.year)
            # We go to the next year
            current = current.replace(year=current.year + 1)
        # We create the parameter and add it to the list
        result.append({"parameter":parameter,"years":years,"id":parameterID})
    # We store the parameters on the redis database
    redis.set(demandParameterID,str(result)) 
    return

def getDemandParameter(globalID,redis):
    '''Get the demand parameters from the redis database'''
    # We get the globalDict to look for the demand
    globalDict = eval(redis.get(str(globalID)).decode()) 
    # We get the demand parameter list from redis
    demandParameterID = eval(redis.get(globalDict["demand"]).decode())["parameters"]
    parameterList = eval(redis.get(demandParameterID).decode())
    data = []
    # We go over each parameter and item in the list
    for item in parameterList:
        row = []
        # We go over each year
        for year in item["years"]: 
            # We get the parameter and make a cell
            parameter = redis.get(item["id"] + str(year))
            row.append({"id":str(item["id"]),"year":year,"parameter":eval(parameter)})
        # We put the row in the result
        data.append({"name":str(item["parameter"]),"data":row})
    return data

def getParameter(globalID,redis):
    '''Internal representation of the parameters for the redis database'''
    # We get the globalDict to look for the demand
    globalDict = eval(redis.get(str(globalID)).decode()) 
    # We get the demand parameter lsit from redis
    demandParameterID = eval(redis.get(globalDict["demand"]).decode())["parameters"]
    parameterList = eval(redis.get(demandParameterID).decode())
    result = []
    # We go over each parameter and item in the list
    for item in parameterList:
        row = {}
        row["parameter"] = item["parameter"]
        # We go over each year
        for year in item["years"]: 
            # We get the parameter and make a cell
            parameter = redis.get(item["id"] + str(year))
            row[year] = eval(parameter) 
        # We add a row to the result
        result.append(row) 
    return result

def setParameter(ID,year,value,redis):
    '''Set the parameter value to a new value'''
    # We create the key
    key = str(ID) + str(year)
    # We change the value on the redis database to a new value
    redis.set(key,str(value))