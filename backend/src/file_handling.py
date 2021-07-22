from uuid import uuid1
import csv
import io
import json

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

def readDemandCSV(id,redis):
    globalDict = eval(redis.get(str(id)).decode())
    fileID = redis.get(globalDict["demand"]).decode()
    result = {}
    rowIDS = eval(redis.get(fileID['id']).decode())
    rows = []
    for rowID in rowIDS:
        row = eval(redis.get(rowID))
        row["rowID"] = rowID
        rows.append(row)
    result["demand"] = rows
    return result