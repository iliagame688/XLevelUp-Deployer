from datetime import datetime


class EventBus:


    def __init__(self):

        self.events = []



    def emit(
        self,
        name,
        data=None
    ):

        event = {

            "event":
                name,

            "data":
                data or {},

            "time":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

        }


        self.events.append(
            event
        )


        return event



    def history(self):

        return self.events



events = EventBus()
