from Core.dashboard.events import write


def deploy():

    result={

        "engine":"XDEPLOY v18",

        "action":"DEPLOY",

        "status":"READY"

    }


    write(
        "DEPLOY_EXECUTED",
        result
    )


    return result

