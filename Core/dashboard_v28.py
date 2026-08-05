
from Core.deploy.engine import deploy
from Core.deploy.rollback import rollback



def status():

    return {

    "engine":
    "XDEPLOY v28",

    "status":
    "ONLINE",

    "modules":
    [
    "Git Sync",
    "Deploy",
    "Snapshot",
    "Rollback"
    ]

    }


