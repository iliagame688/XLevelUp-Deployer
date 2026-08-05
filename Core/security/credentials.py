import json

from pathlib import Path


FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/credentials.json"
)



def save(data):

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





def load():

    if not FILE.exists():

        return []


    return json.loads(

        FILE.read_text(
            encoding="utf-8"
        )

    )



def add(
    account,
    provider,
    credential_id
):

    data = load()


    item = {

        "account":
            account,

        "provider":
            provider,

        "credential_id":
            credential_id,

        "status":
            "UNKNOWN"

    }


    data.append(item)


    save(data)


    return item
