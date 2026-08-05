import datetime

from Core.workspace.manager import get_workspace
from Core.watcher.engine import state



def status():

    return {

    "engine":
    "XDEPLOY v30",

    "status":
    "ONLINE",

    "time":
    str(datetime.datetime.now()),

    "workspace":{

        "path":
        get_workspace(),

        "files":
        state()["files"],

        "status":
        "WATCHING"

    },


    "modules":[

        "AI",
        "Watcher",
        "Snapshot",
        "Deploy",
        "Rollback",
        "Git Engine"

    ]

    }
