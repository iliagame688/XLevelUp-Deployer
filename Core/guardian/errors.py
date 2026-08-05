import json
from pathlib import Path
from datetime import datetime


FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/errors.json"
)



def log_error(
    module,
    error,
    detail=""
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


    item = {

        "module": module,

        "error": str(error),

        "detail": detail,

        "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    }


    data.append(item)


    FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    FILE.write_text(
        json.dumps(
            data[-100:],
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


    return item
