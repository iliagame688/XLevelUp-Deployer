import json
from pathlib import Path
from datetime import datetime


FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/audit.json"
)



def record(
    action,
    status="OK"
):

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


    data.append({

        "action": action,

        "status": status,

        "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    })


    FILE.write_text(

        json.dumps(
            data[-200:],
            indent=4,
            ensure_ascii=False
        ),

        encoding="utf-8"

    )
