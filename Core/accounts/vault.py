import json

from pathlib import Path


FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/accounts.json"
)



def read():

    if not FILE.exists():

        return {

            "accounts": [],
            "active": None

        }


    return json.loads(

        FILE.read_text(
            encoding="utf-8"
        )

    )





def write(data):

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
