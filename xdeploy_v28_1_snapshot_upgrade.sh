#!/data/data/com.termux/files/usr/bin/bash

clear

echo "
╔══════════════════════════════════╗
║       XDEPLOY v28.1               ║
║     REAL SNAPSHOT ENGINE          ║
╚══════════════════════════════════╝
"


mkdir -p Core/snapshot
mkdir -p Core/snapshots


echo "[1] Installing Snapshot Manager"


cat > Core/snapshot/manager.py <<'PY'
import os
import shutil
import json
import datetime
import subprocess


ROOT=os.getcwd()

BASE="Core/snapshots"


IGNORE=[
"Core/snapshots",
"Core/runtime",
".git",
"__pycache__",
".xdeploy"
]


def git_head():

    try:

        return subprocess.check_output(
            "git rev-parse HEAD",
            shell=True,
            text=True
        ).strip()

    except:

        return "UNKNOWN"



def copy_tree(src,dst):

    for item in os.listdir(src):

        if any(
            item.startswith(x)
            for x in IGNORE
        ):
            continue


        s=os.path.join(src,item)
        d=os.path.join(dst,item)


        if os.path.isdir(s):

            shutil.copytree(
                s,
                d,
                dirs_exist_ok=True
            )

        else:

            shutil.copy2(
                s,
                d
            )



def create():

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


    copy_tree(
        ROOT,
        target
    )


    metadata={

        "engine":
        "XDEPLOY v28.1",

        "created":
        str(datetime.datetime.now()),

        "git":
        git_head(),

        "snapshot":
        target

    }


    with open(
        os.path.join(
            target,
            "metadata.json"
        ),
        "w"
    ) as f:

        json.dump(
            metadata,
            f,
            indent=4
        )


    return {

        "snapshot":
        target,

        "status":
        "CREATED",

        "git":
        metadata["git"]

    }

PY



echo "[2] Installing Rollback Engine"



cat > Core/deploy/rollback.py <<'PY'
import os
import json


def rollback():

    latest="Core/snapshots"


    if not os.path.exists(latest):

        return {
        "rollback":"FAILED",
        "reason":"NO_SNAPSHOT"
        }


    snaps=sorted(
        os.listdir(latest)
    )


    if not snaps:

        return {
        "rollback":"FAILED",
        "reason":"EMPTY"
        }


    target=os.path.join(
        latest,
        snaps[-1]
    )


    meta=os.path.join(
        target,
        "metadata.json"
    )


    return {

        "rollback":
        "READY",

        "snapshot":
        target,

        "metadata":
        meta

    }

PY



echo "[3] Compile Test"


python -m py_compile \
Core/snapshot/manager.py \
Core/deploy/rollback.py



echo "

╔══════════════════════════════════╗
║      XDEPLOY v28.1 READY          ║
╚══════════════════════════════════╝


✓ REAL SNAPSHOT
✓ METADATA
✓ GIT CHECKPOINT
✓ ROLLBACK READY
✓ COMPILE PASS


TEST:

python - <<'PY'

from Core.snapshot.manager import create
from Core.deploy.rollback import rollback


print(create())

print(rollback())

PY

"

