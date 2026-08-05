import json

from pathlib import Path
from datetime import datetime


FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/bootstrap_history.json"
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
