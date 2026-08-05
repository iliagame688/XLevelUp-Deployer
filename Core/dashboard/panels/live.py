from rich.panel import Panel


def live_panel(events):


    text = ""


    for item in events:


        text += (

            f'{item["time"]} '

            f'{item["status"]} '

            f'{item["event"]}\n'

        )


    if not text:

        text = "Waiting events..."



    return Panel(

        text,

        title="LIVE OPERATIONS"

    )

