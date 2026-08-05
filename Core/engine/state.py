import json
from pathlib import Path


STATE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/state.json"
)


DEFAULT = {
    "total_files": 0,
    "added": 0,
    "modified": 0,
    "deleted": 0,
    "last_file": None
}



def load():

    data = DEFAULT.copy()


    if STATE.exists():

        try:

            old = json.loads(
                STATE.read_text(
                    encoding="utf-8"
                )
            )

            if isinstance(old, dict):

                data.update(old)

        except:
            pass


    save(data)

    return data



def save(data):

    STATE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    STATE.write_text(
        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )



def update(event):

    data = load()


    data["last_file"] = event["file"]


    if event["type"] == "CREATED":
        data["added"] += 1


    elif event["type"] == "MODIFIED":
        data["modified"] += 1


    elif event["type"] == "DELETED":
        data["deleted"] += 1


    save(data)
