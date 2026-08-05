import json
from pathlib import Path
from datetime import datetime


EVENT_FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/intelligence/data/events.json"
)



def load():

    if not EVENT_FILE.exists():
        return []

    try:

        return json.loads(
            EVENT_FILE.read_text(
                encoding="utf-8"
            )
        )

    except:

        return []



def push(
    source,
    event,
    payload=None
):

    data = load()


    item = {

        "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "source":
            source,

        "event":
            event,

        "payload":
            payload or {}

    }


    data.append(item)


    EVENT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    EVENT_FILE.write_text(
        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


    return item



def history():

    return load()
