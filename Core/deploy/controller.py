
from Core.workspace.manager import get_workspace

from Core.snapshot.manager import create

from Core.git_engine.sync import sync



def deploy():


    workspace=get_workspace()["path"]


    snapshot=create(
    workspace
    )


    git=sync()


    return {

    "engine":
    "XDEPLOY v28.2",

    "deploy":
    "DONE",

    "workspace":
    workspace,

    "snapshot":
    snapshot,

    "git":
    git

    }

