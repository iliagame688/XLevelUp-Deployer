import json
from pathlib import Path
from datetime import datetime


STATUS = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/github_status.json"
)



def check_connection(
    token
):

    result = {

        "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "connected":
            False,

        "user":
            None,

        "repos":
            0,

        "permission":
            "UNKNOWN",

        "status":
            ""

    }


    if not token:

        result["status"] = "NO_TOKEN"

        return save(result)



    # آماده برای اتصال API واقعی
    # در مرحله بعد درخواست HTTP اضافه می‌شود

    result["status"] = "TOKEN_READY"


    return save(result)



def save(data):

    STATUS.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    STATUS.write_text(
        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    return data



def status():

    if not STATUS.exists():

        return {}

    return json.loads(
        STATUS.read_text(
            encoding="utf-8"
        )
    )
