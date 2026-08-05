from Core.live.session import session


class TerminalRenderer:



    def render(self):

        print(
            "\n╭──────── XCONTROL LIVE CENTER ────────╮"
        )


        print(
            "│ LIVE OPERATIONS"
        )


        print(
            "╰──────────────────────────────────────╯"
        )


        for item in session.history():

            icon = "✓"

            if item["status"] == "RUNNING":

                icon = "⟳"


            elif item["status"] == "FAILED":

                icon = "✗"


            print(
                f'{item["time"]} {icon} '
                f'{item["operation"]} '
                f'- {item["detail"]}'
            )



renderer = TerminalRenderer()
