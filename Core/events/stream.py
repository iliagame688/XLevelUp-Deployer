
import os
import json
from datetime import datetime


FILE="runtime/events/live.json"



def push(event):

    os.makedirs(
        "runtime/events",
        exist_ok=True
    )


    data=[]


    if os.path.exists(FILE):

        with open(FILE) as f:
            data=json.load(f)



    data.append({

        "time":
        str(datetime.now()),

        "event":
        event

    })


    with open(FILE,"w") as f:

        json.dump(
            data,
            f,
            indent=4
        )



def read():

    if not os.path.exists(FILE):

        return []


    with open(FILE) as f:

        return json.load(f)

