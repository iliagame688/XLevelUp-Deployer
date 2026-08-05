from datetime import datetime


class TerminalUI:


    def header(self):

        print(
"""
╭──────────────────────────╮
│ XLEVELUP DEPLOYER v5     │
│ CONTROL CENTER           │
╰──────────────────────────╯
"""
        )


    def event(self, text):

        now = datetime.now().strftime(
            "%H:%M:%S"
        )

        print(
            f"[{now}] {text}"
        )



terminal = TerminalUI()
