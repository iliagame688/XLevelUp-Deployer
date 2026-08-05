import os
import shutil
import datetime
import json


IGNORE=[
".git",
"Core/runtime",
"Core/snapshots",
"__pycache__"
]


def create(path):

    name=datetime.datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    target=os.path.join(
        "Core/snapshots",
        name
    )


    os.makedirs(
        target,
        exist_ok=True
    )


    for item in os.listdir(path):

        if item in IGNORE:

            continue


        src=os.path.join(
            path,
            item
        )

        dst=os.path.join(
            target,
            item
        )


        if os.path.isdir(src):

            shutil.copytree(
                src,
                dst,
                dirs_exist_ok=True
            )

        else:

            shutil.copy2(
                src,
                dst
            )


    meta={

    "snapshot":
    target,

    "source":
    path,

    "engine":
    "XDEPLOY v30"

    }


    with open(
        os.path.join(
            target,
            "metadata.json"
        ),
        "w"
    ) as f:

        json.dump(
            meta,
            f,
            indent=4
        )


    return meta
