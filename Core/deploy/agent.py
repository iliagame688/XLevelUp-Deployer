
from Core.watcher.snapshot import snapshot


def deploy_check():

    return {

    "deploy":
    "READY",

    "snapshot":
    snapshot()

    }


if __name__=="__main__":

    print(deploy_check())

