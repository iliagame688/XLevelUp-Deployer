
from Core.ai.commander import decide
from Core.deploy.preflight import scan
from Core.snapshot.manager import create
from Core.events.live import emit



def deploy():


    check=scan()


    if check["compile"]!="PASS":


        return {

        "status":"BLOCKED",

        "reason":"PREFLIGHT_ERROR",

        "details":check

        }



    ai=decide()


    snap=create()


    emit(
    "DEPLOY_READY",
    snap
    )


    return {


    "status":"READY",

    "ai":ai,

    "snapshot":snap


    }

