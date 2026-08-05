import json
import datetime
import os


STATE="Core/data/remote_state.json"


def save(data):

    os.makedirs(
        "Core/data",
        exist_ok=True
    )

    with open(
        STATE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


def deploy(target="LOCAL"):

    result={

        "engine":"XDEPLOY v12",

        "target":target,

        "status":"READY",

        "time":str(
            datetime.datetime.now()
        )

    }


    save(result)

    return result



def rollback():

    result={

        "engine":"XDEPLOY v12",

        "action":"ROLLBACK",

        "status":"READY",

        "time":str(
            datetime.datetime.now()
        )

    }


    save(result)

    return result


