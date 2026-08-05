from datetime import datetime
from Core.workspace.watcher import scan


def dashboard():

    return {

    "engine":"XDEPLOY v20",

    "status":"ONLINE",

    "time":str(datetime.now()),

    "workspace_files":len(scan()),

    "modules":[
        "Workspace Manager",
        "Smart Watcher",
        "Deploy Agent",
        "Rollback",
        "AI Recovery"
    ]

    }


if __name__=="__main__":
    print(dashboard())

