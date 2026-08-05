from Core.dashboard.events import write


def rollback():

    result={

        "engine":"XDEPLOY v18",

        "action":"ROLLBACK",

        "status":"READY"

    }


    write(
        "ROLLBACK_EXECUTED",
        result
    )


    return result

