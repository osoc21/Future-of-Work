from uuid import uuid1
import pandas as pd


def writeCSV(files,names,redis):
    id = uuid1()
    for file,name in zip(files,names):
        df = pd.read_csv(file)
        name = str(id) + "-" + names
        print(name)
        redis.set(str(id) + "-" + names,df.to_msgpack(compress='zlib'))
    return id

def readCSV(id,name,redis):
    return pd.read_msgpack(redis.get(str(id)+ "-" + name))