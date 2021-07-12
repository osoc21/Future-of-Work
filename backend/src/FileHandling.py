from uuid import uuid1
  


def handleFile(file,redis,id = False):
    if not(id):
        id = uuid1()
    
    return id