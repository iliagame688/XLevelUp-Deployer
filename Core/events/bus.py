import json
import os
from datetime import datetime


FILE="Core/runtime/events.json"


def emit(event,data):

    os.makedirs(
        "Core/runtime",
        exist_ok=True
    )


    logs=[]

    if os.path.exists(FILE):

        logs=json.load(open(FILE))


    logs.append(
    {
    "event":event,
    "data":data,
    "time":str(datetime.now())
    }
    )


    json.dump(
        logs[-200:],
        open(FILE,"w"),
        indent=4
    )


def events():

    if not os.path.exists(FILE):
        return []

    return json.load(open(FILE))

