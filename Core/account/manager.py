import json
from pathlib import Path


FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/account.json"
)


def save(account):

    FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    FILE.write_text(
        json.dumps(
            account,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


def load():

    if not FILE.exists():

        return {}

    return json.loads(
        FILE.read_text(
            encoding="utf-8"
        )
    )


def connected():

    data = load()

    return bool(
        data.get(
            "username"
        )
    )
