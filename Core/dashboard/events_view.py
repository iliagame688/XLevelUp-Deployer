import json
from pathlib import Path

from rich.panel import Panel


EVENT_FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/events.json"
)



def get_events():

    if not EVENT_FILE.exists():

        return "No events"



    try:

        events = json.loads(
            EVENT_FILE.read_text(
                encoding="utf-8"
            )
        )


    except:

        return "No events"



    lines = []


    for e in events[-8:]:

        lines.append(

            f"{e.get('time')} "
            f"{e.get('type')} "
            f"{e.get('file')}"

        )


    return "\n".join(lines)



def event_panel():

    return Panel(
        get_events(),
        title="LIVE EVENTS"
    )
