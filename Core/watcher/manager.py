
from Core.watcher.config import load,save


def set_workspace(path):

    save(
        {
        "path":path
        }
    )

    return {
    "watch_path":path,
    "status":"UPDATED"
    }



def info():

    return load()

