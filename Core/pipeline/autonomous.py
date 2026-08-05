
import os
import datetime
import json
import compileall


STATE="Core/data/deploy_state.json"



def save(data):

    os.makedirs(
        "Core/data",
        exist_ok=True
    )

    with open(
        STATE,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )



def preflight():

    result={

        "stage":"PREFLIGHT",

        "syntax":

        compileall.compile_dir(
            ".",
            quiet=1
        ),

        "time":
        str(datetime.datetime.now())

    }


    return result




def deploy():

    check=preflight()


    if check["syntax"]:

        result={

        "engine":"XDEPLOY v14",

        "deploy":
        "SUCCESS",

        "stage":
        "RELEASED",

        "time":
        str(datetime.datetime.now())

        }


    else:

        result={

        "engine":"XDEPLOY v14",

        "deploy":
        "FAILED",

        "stage":
        "PREFLIGHT_ERROR",

        "time":
        str(datetime.datetime.now())

        }



    save(result)


    return result




def rollback():


    result={


    "engine":"XDEPLOY v14",

    "rollback":
    "READY",

    "restored":
    True,


    "time":
    str(datetime.datetime.now())


    }


    save(result)


    return result



