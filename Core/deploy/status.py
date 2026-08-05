import json
from pathlib import Path
from datetime import datetime


FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/deploy.json"
)



def update(
    status,
    message
):

    data = {

        "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "status":
            status,

        "message":
            message

    }


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


    return data




def get():

    if not FILE.exists():

        return {
            "status":
                "IDLE"
        }


    return json.loads(
        FILE.read_text(
            encoding="utf-8"
        )
    )
