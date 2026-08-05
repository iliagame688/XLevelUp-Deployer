import os
import json


def rollback():

    latest="Core/snapshots"


    if not os.path.exists(latest):

        return {
        "rollback":"FAILED",
        "reason":"NO_SNAPSHOT"
        }


    snaps=sorted(
        os.listdir(latest)
    )


    if not snaps:

        return {
        "rollback":"FAILED",
        "reason":"EMPTY"
        }


    target=os.path.join(
        latest,
        snaps[-1]
    )


    meta=os.path.join(
        target,
        "metadata.json"
    )


    return {

        "rollback":
        "READY",

        "snapshot":
        target,

        "metadata":
        meta

    }

