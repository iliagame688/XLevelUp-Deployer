from datetime import datetime

EVENTS=[]


def push(event,data):

    EVENTS.append({

        "event":event,
        "data":data,
        "time":str(datetime.now())

    })


def get_events():

    return EVENTS[-50:]
