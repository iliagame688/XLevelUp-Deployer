import json

from pathlib import Path
from datetime import datetime

from Core.health.recovery import analyze



FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/health_history.json"
)



def save(data):

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


    data["time"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    items.append(data)


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



def check(status, error=None):


    result = {

        "status":
            status,

        "online":
            status == "SUCCESS"

    }


    if error:

        result["recovery"] = analyze(
            error
        )


    save(result)


    return result
