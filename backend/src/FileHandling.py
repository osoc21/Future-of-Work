from uuid import uuid1
import pandas as  pd
import io

def writeCSV(files,names,redis):
    id = uuid1()
    print(id)
    for file,name in zip(files,names):
        df = pd.read_csv(file)
        buffer = io.BytesIO()
        buffer.seek(0)
        df.to_parquet(buffer, compression='gzip')
        curName = str(id) + "-" + name
        redis.set(str(id) + "-" + curName,buffer.read())
    return "Done"

def readCSV(id,name,redis):
    buffer = io.BytesIO(redis.get(str(id) + "-" + name))
    buffer.seek(0)
    return pd.read_parquet(buffer)