import datetime


EVENTS=[]


def emit(name,data):

    EVENTS.append({

        "event":name,

        "data":data,

        "time":str(
            datetime.datetime.now()
        )

    })


    return EVENTS[-1]



def history():

    return EVENTS

