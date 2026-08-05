
from Core.dashboard.live.event_bus import bus


class LiveView:


    def render(self):

        print(
"""
╭──────── LIVE DEPLOY ────────╮
"""
        )


        events = bus.get()


        for event in events[-10:]:


            icon = "✓"


            if event["level"] == "ERROR":

                icon = "!"


            elif event["level"] == "DEPLOY":

                icon = "▶"


            print(

                f"{icon} {event['message']}"

            )


        print(
"""
╰─────────────────────────────╯
"""
        )



live_view = LiveView()

