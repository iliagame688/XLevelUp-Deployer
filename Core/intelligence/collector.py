import json
from pathlib import Path
from datetime import datetime


DATA = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/intelligence/data/errors.json"
)



def load():

    if not DATA.exists():

        return []

    try:

        return json.loads(
            DATA.read_text(
                encoding="utf-8"
            )
        )

    except:

        return []



def save(data):

    DATA.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    DATA.write_text(
        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )



def report(
    module,
    error
):

    logs = load()


    item = {

        "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "module":
            module,

        "error":
            str(error)

    }


    logs.append(item)

    save(logs)


    return item



def history():

    return load()
