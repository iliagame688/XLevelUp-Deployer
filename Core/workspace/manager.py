import json
import os

CONFIG="Core/config/workspace.json"


def get_workspace():

    if not os.path.exists(CONFIG):
        return None

    with open(CONFIG) as f:
        return json.load(f)



def set_workspace(path):

    data=get_workspace() or {}

    data["path"]=path

    with open(CONFIG,"w") as f:
        json.dump(data,f,indent=4)

    return {
        "workspace":path,
        "status":"UPDATED"
    }
