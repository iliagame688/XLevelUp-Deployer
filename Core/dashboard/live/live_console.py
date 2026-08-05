from datetime import datetime


class LiveConsole:

    def __init__(self):

        self.events = []


    def push(
        self,
        message,
        level="INFO",
        progress=0
    ):

        self.events.append({

            "time":
                datetime.now().strftime(
                    "%H:%M:%S"
                ),

            "message":
                message,

            "level":
                level,

            "progress":
                progress

        })

        self.render()



    def render(self):

        print()

        print(
            "╭──────── XLEVELUP LIVE DASHBOARD ────────╮"
        )


        if self.events:

            last = self.events[-1]


            print(
                "STATUS:",
                last["message"]
            )


            print(
                "LEVEL:",
                last["level"]
            )


            print(
                "PROGRESS:",
                str(last["progress"]) + "%"
            )


        print()


        for e in self.events[-5:]:

            print(
                f'[{e["time"]}] '
                f'{e["message"]} '
                f'{e["progress"]}%'
            )


        print(
            "╰────────────────────────────────────────╯"
        )



live_console = LiveConsole()
