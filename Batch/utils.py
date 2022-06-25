import uuid

def generateLink(name):
    link = str(uuid.uuid4()).replace('-', '')[:8]
    return link[:4] + 'batch:' + str(name).lower() + link[4:]
