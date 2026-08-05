import os
import shutil
import json
import time
from datetime import datetime


BASE=os.getcwd()

SNAPSHOT_ROOT=os.path.join(
    BASE,
    "Core",
    "runtime",
    "snapshots"
)


IGNORE=[
    "__pycache__",
    ".git",
    "runtime",
    "snapshots",
    ".env",
    "*.pyc",
    "logs"
]


def allowed(path):

    for x in IGNORE:
        if x in path:
            return False

    return True



def create_snapshot():

    sid=datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    target=os.path.join(
        SNAPSHOT_ROOT,
        sid
    )


    os.makedirs(
        target,
        exist_ok=True
    )


    count=0


    for root,dirs,files in os.walk(BASE):

        dirs[:]=[
            d for d in dirs
            if allowed(
                os.path.join(root,d)
            )
        ]


        for f in files:

            src=os.path.join(root,f)


            if not allowed(src):
                continue


            rel=os.path.relpath(
                src,
                BASE
            )


            dst=os.path.join(
                target,
                rel
            )


            os.makedirs(
                os.path.dirname(dst),
                exist_ok=True
            )


            shutil.copy2(
                src,
                dst
            )


            count+=1


    data={
        "engine":"XDEPLOY v15",
        "snapshot":sid,
        "files":count,
        "status":"READY",
        "time":str(datetime.now())
    }


    with open(
        "Core/snapshot/latest.json",
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


    return data



if __name__=="__main__":

    print(create_snapshot())

