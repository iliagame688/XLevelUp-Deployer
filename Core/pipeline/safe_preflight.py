

from Core.recovery.pipeline_guard import scan


def run():


    errors=scan()


    if errors:


        return {

        "status":"BLOCKED",

        "reason":"SYNTAX_ERRORS",

        "errors":errors

        }



    return {


    "status":"READY",

    "reason":"CLEAN"


    }


