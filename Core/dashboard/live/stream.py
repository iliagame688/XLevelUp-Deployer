
from Core.dashboard.live.event_bus import bus



class LiveStream:


    def push(self, message, level="INFO"):

        bus.emit(
            message,
            level
        )


    def read(self):

        return bus.get()




stream = LiveStream()

