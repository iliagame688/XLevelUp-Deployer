EVENTS=[]


def emit(name,data):

    EVENTS.append(
        {
        "event":name,
        "data":data
        }
    )


def get():

    return EVENTS
