
from Core.workspace.manager import get_workspace

from Core.snapshot.create import create

from Core.git_engine.sync import sync



def deploy():


    workspace=get_workspace()


    if not workspace:

        return {

        "status":
        "FAILED",

        "reason":
        "NO_WORKSPACE"

        }


    snapshot=create(
        workspace
    )


    git=sync(
        "XDEPLOY v30 AUTO DEPLOY"
    )


    return {


    "status":
    "DEPLOYED",

    "workspace":
    workspace,

    "snapshot":
    snapshot,

    "git":
    git

    }

