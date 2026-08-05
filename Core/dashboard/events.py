import json
import os
import datetime


FILE="Core/runtime/events.json"



def write(event,data):

    os.makedirs(
        "Core/runtime",
        exist_ok=True
    )


    logs=[]


    if os.path.exists(FILE):

        try:
            logs=json.load(
                open(FILE)
            )
        except:
            logs=[]


    logs.append({

        "event":event,

        "data":data,

        "time":
        str(datetime.datetime.now())

    })


    json.dump(
        logs[-100:],
        open(FILE,"w"),
        indent=4
    )



def read():

    if not os.path.exists(FILE):

        return []


    return json.load(
        open(FILE)
    )

