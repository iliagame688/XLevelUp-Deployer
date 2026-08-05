import json
from pathlib import Path
from datetime import datetime


SNAPSHOT = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/workspace_snapshot.json"
)



def save_snapshot(files):

    data = {

        "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "count":
            len(files),

        "files":
            files
    }


    SNAPSHOT.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    SNAPSHOT.write_text(
        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


    return data



def load_snapshot():

    if not SNAPSHOT.exists():

        return None


    try:

        return json.loads(
            SNAPSHOT.read_text(
                encoding="utf-8"
            )
        )

    except:

        return None
