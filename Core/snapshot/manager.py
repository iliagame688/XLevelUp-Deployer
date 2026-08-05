
import os
import shutil
import datetime
import json


BASE="Core/snapshots"


IGNORE=[
".git",
"Core",
"__pycache__"
]



def create(project):

    name=datetime.datetime.now().strftime(
    "%Y%m%d_%H%M%S"
    )


    target=os.path.join(
    BASE,
    name
    )


    os.makedirs(
    target,
    exist_ok=True
    )


    for item in os.listdir(project):

        if item in IGNORE:
            continue


        src=os.path.join(
            project,
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

    "engine":
    "XDEPLOY v28.2",

    "workspace":
    project,

    "snapshot":
    target

    }


    with open(
    os.path.join(target,"metadata.json"),
    "w"
    ) as f:

        json.dump(
        meta,
        f,
        indent=4
        )


    return meta


