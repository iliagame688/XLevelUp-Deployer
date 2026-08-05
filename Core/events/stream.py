import json
import os
import datetime


FILE="Core/data/events.json"



def emit(event,data):

    os.makedirs(
        "Core/data",
        exist_ok=True
    )


    events=[]


    if os.path.exists(FILE):

        with open(FILE) as f:
            events=json.load(f)


    events.append({

        "event":
        event,

        "data":
        data,

        "time":
        str(datetime.datetime.now())

    })


    with open(FILE,"w") as f:

        json.dump(
            events[-100:],
            f,
            indent=4
        )



def get():

    if not os.path.exists(FILE):

        return []


    with open(FILE) as f:

        return json.load(f)
