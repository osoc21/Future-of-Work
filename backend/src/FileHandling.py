from uuid import uuid1
import pandas as pd 
import io
import json

def writeCSVs(files,names,redis):
    globalID = str(uuid1())
    files = {}
    for file,name in zip(files,names):
        df = pd.read_csv(file)
        ids = []
        dataID = str(uuid1())
        for _,row in df.iterrows():
            id = str(uuid1())
            ids.append(id) 
            redis.set(id,row.to_json())
        redis.set(dataID,str(ids)) 
        files[name] = {'id':dataID} 
    redis.set(globalID,json.dumps(files,indent=0))
    return globalID
 
def readCSV(id,redis):
    filesID = json.load(redis.get(id))
    for fileID in filesID:
        rowIDS = json.load(redis.get(fileID))
        df = []
        for rowID in rowIDS:
            df = pd.read_json()
    return 