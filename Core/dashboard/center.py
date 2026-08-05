
from Core.watcher.manager import status


def dashboard():

    return {

    "engine":
    "XDEPLOY v28.2",

    "status":
    "ONLINE",

    "workspace":
    status(),

    "modules":[
    "Watcher",
    "Snapshot",
    "Deploy",
    "Git Engine",
    "Security"
    ]

    }

