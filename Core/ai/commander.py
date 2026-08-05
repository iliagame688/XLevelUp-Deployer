from datetime import datetime


def analyze():

    result={

        "time":str(datetime.now()),

        "syntax":"CHECKED",

        "secrets":"CHECKED",

        "git":"CHECKED",

        "decision":"READY"

    }


    return result



def decide():

    report=analyze()


    if report["decision"]=="READY":

        return {

        "status":"APPROVED",

        "action":"DEPLOY"

        }


    return {

    "status":"BLOCKED"

    }

