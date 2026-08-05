
import datetime
import os

from Core.watcher.config import load



def status():

    cfg=load()

    count=0

    try:

        for root,dirs,files in os.walk(
            cfg["path"]
        ):
            count+=len(files)

    except:
        pass


    return {

    "engine":"XDEPLOY v27",

    "status":"ONLINE",

    "time":
    str(datetime.datetime.now()),


    "workspace":
    {
    "path":cfg["path"],
    "files":count,
    "status":"WATCHING"
    },


    "modules":
    [
    "AI Brain",
    "Watcher",
    "Deploy",
    "Recovery",
    "Rollback",
    "Git Engine"
    ]

    }

