import json

from pathlib import Path
from datetime import datetime


FILE = Path(
"/storage/emulated/0/XLevelUp-Deployer/Core/data/repair_history.json"
)



def save(item):

    data = []


    if FILE.exists():

        try:

            data = json.loads(
                FILE.read_text(
                    encoding="utf-8"
                )
            )

        except:

            data = []


    item["time"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    data.append(item)


    FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    FILE.write_text(
        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )
