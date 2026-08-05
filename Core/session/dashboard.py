
import time


class SessionDashboard:


    def start(self, result):


        print("""
╭──────────────────────────╮
│ XLEVELUP SESSION CENTER  │
╰──────────────────────────╯
""")


        print(
            "ENGINE   : ONLINE"
        )


        print(
            "DEPLOY   :",
            result.get(
                "status"
            )
        )


        print(
            "PIPELINE :",
            result.get(
                "pipeline"
            )
        )


        print("""
╭──────────────────────────╮
│ [1] New Deploy            │
│ [2] View Session          │
│ [3] Exit                 │
╰──────────────────────────╯
""")


        try:

            choice = input(
                "Choice: "
            )


        except EOFError:

            choice = "3"


        return choice




dashboard = SessionDashboard()

