
from datetime import datetime


def analyze(error):

    return {

    "error":error,

    "action":
    "GENERATE_PATCH",

    "confidence":
    99,

    "time":
    str(datetime.now())

    }

