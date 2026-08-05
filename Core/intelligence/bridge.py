from Core.engine.events import subscribe

from Core.intelligence.events import push

from Core.intelligence.analyzer import analyze



def receive(event):

    push(
        event["source"],
        event["event"],
        event.get("data")
    )


    if event["event"] == "ERROR":

        analyze(

            event["source"],

            event.get(
                "data",
                {}
            ).get(
                "error",
                "Unknown"
            )

        )



def connect():

    subscribe(
        receive
    )

    return True
