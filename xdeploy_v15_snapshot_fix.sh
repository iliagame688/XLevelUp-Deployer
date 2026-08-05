#!/data/data/com.termux/files/usr/bin/bash

set -e

PROJECT="/storage/emulated/0/XLevelUp-Deployer"

cd "$PROJECT"

echo "
╔════════════════════════════════════╗
║        XDEPLOY v15                 ║
║     SMART SNAPSHOT ENGINE          ║
╚════════════════════════════════════╝
"


mkdir -p Core/snapshot
mkdir -p Core/runtime/snapshots


echo "[1] Creating Snapshot Manager"


cat > Core/snapshot/manager.py <<'PY'
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

PY



echo "[2] Snapshot Test"


python - <<'PY'

from Core.snapshot.manager import create_snapshot

print(
    create_snapshot()
)

PY



echo "[3] Git Update"


git add .

git commit \
-m "XDEPLOY v15 smart snapshot engine" \
|| true


git push origin main || true



echo "
╔════════════════════════════════════╗
║      XDEPLOY v15 READY              ║
╚════════════════════════════════════╝


FIXED:

✓ Snapshot Loop Protection
✓ Runtime Excluded
✓ Pycache Excluded
✓ Recursive Block
✓ Dashboard Compatible


NEXT:

Connect Snapshot Button
Add Restore Engine
Add AI Rollback

"

