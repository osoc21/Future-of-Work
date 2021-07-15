from uuid import uuid1
import pandas as pd 
import io

def writeCSV(files,names,redis):
    result = {'globalID':str(uuid1())}
    globalID = str(uuid1())
    for file,name in zip(files,names):
        df = pd.read_csv(file)
        ids = []
        dataID = str(uuid1())
        for _,row in df.iterrows():
            id = str(uuid1())
            ids.append(id) 
            redis.set(id,row.to_json()) 
        df['id'] = ids 
        redis.set(dataID,str(ids)) 
        result[name] = {'id':dataID,'Data':df.to_dict()}
    return result

def readCSV(id,name,redis):
    buffer = io.BytesIO(redis.get(str(id) + "-" + name))
    buffer.seek(0)
    return pd.read_parquet(buffer)