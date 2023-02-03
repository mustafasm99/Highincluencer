import uuid
def genrate_cod():
    code=str(uuid.uuid4()).replace("-","")[:12]
    return code