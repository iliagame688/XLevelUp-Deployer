import datetime


def analyze(action):

    return {

        "ai":
        "READY",

        "action":
        action,

        "decision":
        "APPROVED",

        "confidence":
        99,

        "time":
        str(datetime.datetime.now())

    }
