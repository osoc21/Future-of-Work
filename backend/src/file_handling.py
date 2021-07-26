from uuid import uuid1
import csv
import io
import json 
import datetime

def writeCSVs(supplyFiles,supplyNames,demandFile,redis):
    globalID = str(uuid1())
    supplyID = str(uuid1())
    demandID = str(uuid1())
    # Supply mapping
    filesIDs = {}
    for file,name in zip(supplyFiles,supplyNames):
        ids = []
        dataID = str(uuid1())
        with io.TextIOWrapper(file, encoding='utf-8') as text_file:
            csvReader = csv.DictReader(text_file, delimiter=',')
            for row in csvReader:
                id = str(uuid1())
                ids.append(id)
                redis.set(id,str(row))
        redis.set(dataID,str(ids))
        filesIDs[name] = {'id':dataID}
    redis.set(supplyID,str(filesIDs))
    # Demand mapping
    demandFileID = str(uuid1())
    demandIds = []
    with io.TextIOWrapper(demandFile, encoding='utf-8') as demand_text_file:
        demandCSVReader = csv.DictReader(demand_text_file, delimiter=',')
        for demandRow in demandCSVReader: 
            id = str(uuid1())
            demandIds.append(id)
            redis.set(id,str(demandRow))
        redis.set(demandFileID,str(demandIds))
    # Global mapping 
    redis.set(demandID,str({"csv":demandFileID,"parameters":str(uuid1())}))
    redis.set(globalID,str({"supply":supplyID,"demand":demandID}))
    return globalID 

def readCSVs(id,redis):
    globalDict = eval(redis.get(str(id)).decode())
    filesIDs = eval(redis.get(globalDict["supply"]).decode()) 
    result = {}
    # supply loading
    for fileName in filesIDs:
        fileID = filesIDs[fileName]
        rowIDS = eval(redis.get(fileID['id']).decode())
        rows = []
        for rowID in rowIDS:
            row = eval(redis.get(rowID))
            row["rowID"] = rowID
            rows.append(row)
        result[fileName] = rows
    # demand loading
    demandFileID = eval(redis.get(globalDict["demand"]).decode())["csv"]
    demandRowIDs = eval(redis.get(demandFileID))
    rows = []
    for rowID in demandRowIDs:
        row = eval(redis.get(rowID))
        row["rowID"] = rowID
        rows.append(row)
    result["demand"] = rows
    return result

def writeSupplyCSVs(files,names,redis):
    globalID = str(uuid1())
    filesIDs = {}
    for file,name in zip(files,names):
        ids = []
        dataID = str(uuid1())
        with io.TextIOWrapper(file, encoding='utf-8') as text_file:
            csvReader = csv.DictReader(text_file, delimiter=',')
            for row in csvReader:
                id = str(uuid1())
                ids.append(id)
                redis.set(id,str(row))
        redis.set(dataID,str(ids))
        filesIDs[name] = {'id':dataID}
    supplyID = str(uuid1())
    redis.set(globalID,str({"supply":supplyID,"demand":str(uuid1())}))
    redis.set(supplyID,str(filesIDs))
    return globalID
 
def readSupplyCSVs(id,redis):
    globalDict = eval(redis.get(str(id)).decode())
    filesIDs = eval(redis.get(globalDict["supply"]).decode()) 
    result = {}
    for fileName in filesIDs:
        fileID = filesIDs[fileName]
        rowIDS = eval(redis.get(fileID['id']).decode())
        rows = []
        for rowID in rowIDS:
            row = eval(redis.get(rowID))
            row["rowID"] = rowID
            rows.append(row)
        result[fileName] = rows
    return result

def writeDemandCSV(globalID,file,redis):
    globalDict = eval(redis.get(str(globalID)).decode())
    demandID = globalDict["demand"]
    ids = []
    with io.TextIOWrapper(file, encoding='utf-8') as text_file:
        csvReader = csv.DictReader(text_file, delimiter=',')
        for row in csvReader:
            id = str(uuid1())
            ids.append(id)
            redis.set(id,str(row))
    redis.set(demandID,str(ids))

def readDemandCSV(globalID,redis):
    globalDict = eval(redis.get(str(globalID)).decode()) 
    demandFileID = eval(redis.get(globalDict["demand"]).decode())["csv"]
    demandRowIDs = eval(redis.get(demandFileID))
    rows = [] 
    for rowID in demandRowIDs:
        row = eval(redis.get(rowID)) 
        row["rowID"] = rowID
        rows.append(row)
    return {"demand":rows}

def writeDemandParameter(globalID,parameters,default,redis,horizon = 5):
    globalDict = eval(redis.get(str(globalID)).decode()) 
    demandParameterID = eval(redis.get(globalDict["demand"]).decode())["parameters"]
    
    result = []
    
    for parameter in parameters:
        row = []    
        for _ in range(0,horizon):
            cellID = str(uuid1())
            redis.set(cellID,str(default))
            row.append(cellID)
        result.append({parameter:row})
    redis.set(demandParameterID,str(result))

    return

def getDemandParameter(globalID,redis):
    globalDict = eval(redis.get(str(globalID)).decode()) 
    demandParameterID = eval(redis.get(globalDict["demand"]).decode())["parameters"]
    parameterList = eval(redis.get(demandParameterID).decode())
    result = []
    for item in parameterList:
        row = {} 
        for parameter in item:
            for cellID in item[parameter]:
                row[cellID] = eval(redis.get(cellID))
            result.append({parameter:row})
    return result
