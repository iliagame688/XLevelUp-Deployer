import json
from pathlib import Path
from datetime import datetime


QUEUE_FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/deploy_queue.json"
)


def load():

    if not QUEUE_FILE.exists():
        return []

    try:
        return json.loads(
            QUEUE_FILE.read_text(
                encoding="utf-8"
            )
        )

    except:
        return []



def save(data):

    QUEUE_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    QUEUE_FILE.write_text(
        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )



def add(file):

    items = load()

    item = {

        "file": str(file),

        "status": "WAITING",

        "created":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    }

    items.append(item)

    save(items)

    return item



def all():

    return load()
