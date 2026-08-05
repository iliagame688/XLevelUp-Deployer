from datetime import datetime
import uuid


def create(
    file,
    action="MODIFIED",
    provider="LOCAL"
):

    return {

        "id":
            str(uuid.uuid4())[:8],

        "file":
            str(file),

        "action":
            action,

        "provider":
            provider,

        "status":
            "WAITING",

        "created":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    }
