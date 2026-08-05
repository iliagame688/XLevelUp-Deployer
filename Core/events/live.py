import json
import os
from datetime import datetime


FILE="Core/data/events.json"



def emit(event,data):


    os.makedirs(
    "Core/data",
    exist_ok=True
    )


    items=[]


    if os.path.exists(FILE):

        items=json.load(
        open(FILE)
        )


    items.append({

    "event":event,

    "data":data,

    "time":str(datetime.now())

    })


    json.dump(
    items,
    open(FILE,"w"),
    indent=4
    )



def get_events():

    if not os.path.exists(FILE):

        return []

    return json.load(
    open(FILE)
    )

