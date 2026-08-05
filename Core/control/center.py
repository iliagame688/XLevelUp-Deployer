
from Core.workspace.manager import current
from Core.workspace.watcher import scan


def center():

    return {

    "engine":"XDEPLOY v20",

    "workspace":
        current(),

    "files":
        len(scan()),

    "status":
        "ONLINE"

    }


