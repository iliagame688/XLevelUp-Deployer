
from Core.config.settings import load
from Core.watcher.engine import state



def show():

    cfg=load()


    return {

        "engine":
        cfg.get(
        "engine",
        "XDEPLOY v32"
        ),


        "workspace":
        cfg.get(
        "workspace",
        ""
        ),


        "repo":
        cfg.get(
        "repo",
        ""
        ),


        "branch":
        cfg.get(
        "branch",
        "main"
        ),


        "watcher":
        state()

    }

