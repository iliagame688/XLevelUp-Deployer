import json

from pathlib import Path
from datetime import datetime


FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/commit_history.json"
)



def save(data):

    history = []


    if FILE.exists():

        try:

            history = json.loads(
                FILE.read_text(
                    encoding="utf-8"
                )
            )

        except:

            history = []


    data["time"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    history.append(data)


    FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    FILE.write_text(
        json.dumps(
            history,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


    return data




def generate_message(files):

    count = len(files)


    if count == 0:

        return "No changes"



    return (
        f"Auto update {count} file"
        + ("s" if count > 1 else "")
    )
