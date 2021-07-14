from uuid import uuid1
import pandas as pd
import io

def writeCSV(files,names,redis):
    result = {}
    for file,name in zip(files,names):
        df = pd.read_csv(file)
        ids = []
        for _,row in df.iterrows():
            id = uuid1()
            ids.append(id)
            redis.set(str(id),row.to_json())
        result[name] = df.to_json()
    return result

def readCSV(id,name,redis):
    buffer = io.BytesIO(redis.get(str(id) + "-" + name))
    buffer.seek(0)
    return pd.read_parquet(buffer)