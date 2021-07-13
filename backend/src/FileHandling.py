from uuid import uuid1
import pandas as pd
import io

def writeCSV(files,names,redis):
    for file,name in zip(files,names):
        df = pd.read_csv(file)
        print(df.to_json())
    return "Done"

def readCSV(id,name,redis):
    buffer = io.BytesIO(redis.get(str(id) + "-" + name))
    buffer.seek(0)
    return pd.read_parquet(buffer)

def handlePopulation(df,redis):
    for _,row in df.iterrows():
            id = uuid1()
            row.to_json()
            redis.set(str(id),row)
    return 