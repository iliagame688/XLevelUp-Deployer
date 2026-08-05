import os


def rollback():

    root="Core/snapshots"


    if not os.path.exists(root):

        return {
        "rollback":
        "NO SNAPSHOT"
        }


    snaps=sorted(
        os.listdir(root)
    )


    if not snaps:

        return {
        "rollback":
        "EMPTY"
        }


    return {

    "rollback":
    "READY",

    "snapshot":
    snaps[-1]

    }

