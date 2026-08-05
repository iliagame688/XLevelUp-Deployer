from datetime import datetime


def dashboard():

    try:
        from Core.workspace.watcher import scan

        files=len(scan())

    except Exception:
        files=0


    return {

        "engine":"XDEPLOY v23.1",

        "status":"ONLINE",

        "time":str(datetime.now()),


        "workspace":{

            "files":files,

            "status":"WATCHING"

        },


        "modules":[

            "AI Brain",

            "Watcher",

            "Deploy",

            "Recovery",

            "Rollback",

            "Git Engine",

            "Control Plane"

        ],


        "server":{

            "status":"READY",

            "port":8080

        }

    }

