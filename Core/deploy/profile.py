import json

from pathlib import Path
from datetime import datetime


FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/deploy_profile.json"
)



def create(data):

    data["created"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


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



def load():

    if not FILE.exists():

        return {}

    return json.loads(
        FILE.read_text(
            encoding="utf-8"
        )
    )
