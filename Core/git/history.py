import json

from pathlib import Path
from datetime import datetime


FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/git_history.json"
)



def add(event):

    items = []


    if FILE.exists():

        try:
            items = json.loads(
                FILE.read_text(
                    encoding="utf-8"
                )
            )

        except:
            items = []


    event["time"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    items.append(event)


    FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    FILE.write_text(
        json.dumps(
            items,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


    return event
