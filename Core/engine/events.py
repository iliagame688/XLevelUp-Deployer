from datetime import datetime


listeners = []



def subscribe(callback):

    if callback not in listeners:

        listeners.append(callback)



def emit(
    source,
    event,
    data=None
):

    payload = {

        "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "source":
            source,

        "event":
            event,

        "data":
            data or {}

    }


    for callback in listeners:

        try:

            callback(payload)

        except Exception:

            pass


    return payload
