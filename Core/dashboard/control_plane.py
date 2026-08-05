import datetime

from Core.dashboard.events import read
from Core.deploy.controller import deploy
from Core.recovery.controller import rollback


def status():

    return {

        "engine":"XDEPLOY v18",

        "status":"ONLINE",

        "time":
        str(datetime.datetime.now()),

        "modules":[

            "Deploy",

            "Rollback",

            "AI Recovery",

            "Watcher",

            "Git"

        ]

    }



def dashboard():

    return {

        "center":status(),

        "events":read()[-20:]

    }



__all__=[
    "dashboard",
    "deploy",
    "rollback"
]

