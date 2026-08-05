
class EventBus:


    def __init__(self):

        self.events = []

        self.listeners = []



    def subscribe(self, callback):

        if callback not in self.listeners:

            self.listeners.append(
                callback
            )



    def emit(
        self,
        message,
        level="INFO",
        progress=None
    ):

        event = {

            "message":
                message,

            "level":
                level,

            "progress":
                progress

        }


        self.events.append(
            event
        )


        # LIVE BROADCAST

        for listener in self.listeners:

            try:

                listener(
                    event
                )

            except Exception:

                pass



        return event



    def clear(self):

        self.events.clear()



    def get(self):

        return self.events



bus = EventBus()
