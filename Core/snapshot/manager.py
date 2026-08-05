import os
import datetime


def create():

    name = datetime.datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    path = f"Core/snapshots/{name}"

    os.makedirs(
        path,
        exist_ok=True
    )

    return {

        "snapshot": path,

        "status": "CREATED"

    }
