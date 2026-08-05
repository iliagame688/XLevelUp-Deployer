
from Core.dashboard.live.event_bus import bus
import time


class LiveDashboard:


    def __init__(self):

        self.last = None


    def render(self):

        events = bus.get()

        if not events:
            return


        print("\n╭──────── XLEVELUP LIVE DASHBOARD ────────╮")


        for event in events:

            msg = event.get(
                "message",
                ""
            )

            level = event.get(
                "level",
                "INFO"
            )

            progress = event.get(
                "progress",
                0
            )


            bar = ""

            if progress is not None:

                filled = int(progress / 5)

                bar = (
                    "[" 
                    + "█" * filled
                    + "-" * (20-filled)
                    + "] "
                    + str(progress)
                    + "%"
                )


            print(
                f"{level:<8} | {bar} | {msg}"
            )


        print(
            "╰──────────────────────────────────────────╯"
        )



dashboard = LiveDashboard()
