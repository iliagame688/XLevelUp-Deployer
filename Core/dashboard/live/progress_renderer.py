
from Core.dashboard.live.progress import progress



class ProgressRenderer:



    def render(self):


        data = progress.state()


        size = 20


        filled = int(
            size *
            data["progress"]
            /
            100
        )


        bar = (

            "█" * filled

            +

            "░" *
            (
                size-filled
            )

        )


        print(

f"""
╭──── DEPLOY PROGRESS ────╮

Stage:
{data['stage']}

[{bar}]
{data['progress']}%

Status:
{data['status']}

╰─────────────────────────╯
"""

        )





progress_renderer = ProgressRenderer()

