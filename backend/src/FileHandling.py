from uuid import uuid1
import pandas as pd 
import io
import json

def writeCSV(files,names,redis):
    globalID = str(uuid1())
    result = {}
    for file,name in zip(files,names):
        df = pd.read_csv(file)
        ids = []
        dataID = str(uuid1())
        for _,row in df.iterrows():
            id = str(uuid1())
            ids.append(id) 
            redis.set(id,row.to_json())
        redis.set(dataID,str(ids)) 
        result[name] = {'id':dataID} 
    redis.set(globalID,json.dumps(result,indent=0))
    return globalID
 
def readCSV(id,name,redis):
    buffer = io.BytesIO(redis.get(str(id) + "-" + name))
    buffer.seek(0)
    return pd.read_parquet(buffer)