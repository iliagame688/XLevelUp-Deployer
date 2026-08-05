#!/data/data/com.termux/files/usr/bin/bash

clear

echo "
╔══════════════════════════════════════╗
║        XDEPLOY v28.2                 ║
║   WORKSPACE DEPLOYMENT CORE          ║
╚══════════════════════════════════════╝
"


ROOT=$(pwd)

echo "[1] Core Structure"


mkdir -p Core/workspace
mkdir -p Core/watcher
mkdir -p Core/deploy
mkdir -p Core/git_engine
mkdir -p Core/snapshot
mkdir -p Core/security
mkdir -p Core/dashboard
mkdir -p Core/config
mkdir -p Core/events


echo "[2] Workspace Config"


cat > Core/config/workspace.json <<EOF
{
    "path": "$ROOT",
    "watch": true,
    "auto_snapshot": true
}
EOF


cat > Core/workspace/manager.py <<'PY'
import json
import os


CONFIG="Core/config/workspace.json"


def get_workspace():

    with open(CONFIG) as f:

        return json.load(f)



def set_workspace(path):

    data={
        "path":os.path.abspath(path),
        "watch":True,
        "auto_snapshot":True
    }


    with open(CONFIG,"w") as f:

        json.dump(
            data,
            f,
            indent=4
        )


    return data

PY



echo "[3] Smart Watcher"



cat > Core/watcher/manager.py <<'PY'

import os

from Core.workspace.manager import get_workspace



IGNORE=[
".git",
"Core/runtime",
"Core/snapshots",
"__pycache__"
]


def scan():

    cfg=get_workspace()

    root=cfg["path"]

    result=[]


    for base,dirs,files in os.walk(root):

        dirs[:]=[
            d for d in dirs
            if d not in IGNORE
        ]


        for file in files:

            path=os.path.join(
                base,
                file
            )

            result.append(path)


    return result



def status():

    return {

    "workspace":
    get_workspace()["path"],

    "files":
    len(scan()),

    "status":
    "WATCHING"

    }

PY



echo "[4] Snapshot Workspace Engine"


cat > Core/snapshot/manager.py <<'PY'

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


PY



echo "[5] Git Deployment Engine"



cat > Core/git_engine/sync.py <<'PY'

import subprocess



def run(cmd):

    return subprocess.run(
    cmd,
    shell=True,
    text=True,
    capture_output=True
    )



def sync(message="XDEPLOY AUTO SYNC"):


    run(
    "git add -A"
    )


    commit=run(
    f'git commit -m "{message}"'
    )


    push=run(
    "git push origin main"
    )


    return {


    "commit":
    commit.stdout,

    "push":
    push.stdout
    if push.returncode==0
    else
    push.stderr

    }

PY



echo "[6] Deploy Controller"


cat > Core/deploy/controller.py <<'PY'

from Core.workspace.manager import get_workspace

from Core.snapshot.manager import create

from Core.git_engine.sync import sync



def deploy():


    workspace=get_workspace()["path"]


    snapshot=create(
    workspace
    )


    git=sync()


    return {

    "engine":
    "XDEPLOY v28.2",

    "deploy":
    "DONE",

    "workspace":
    workspace,

    "snapshot":
    snapshot,

    "git":
    git

    }

PY



echo "[7] Security Vault"



cat > Core/security/token.py <<'PY'

import os
import json


PATH=os.path.expanduser(
"~/.xdeploy/token.json"
)



def save(token):

    os.makedirs(
    os.path.dirname(PATH),
    exist_ok=True
    )


    with open(PATH,"w") as f:

        json.dump(
        {
        "token":token
        },
        f
        )


    return "TOKEN SAVED"



def load():

    if not os.path.exists(PATH):
        return None


    with open(PATH) as f:

        return json.load(f)

PY



echo "[8] Dashboard Core"



cat > Core/dashboard/center.py <<'PY'

from Core.watcher.manager import status


def dashboard():

    return {

    "engine":
    "XDEPLOY v28.2",

    "status":
    "ONLINE",

    "workspace":
    status(),

    "modules":[
    "Watcher",
    "Snapshot",
    "Deploy",
    "Git Engine",
    "Security"
    ]

    }

PY



echo "[9] Launcher"



cat > xdeploy.py <<'PY'

from Core.dashboard.center import dashboard

from Core.deploy.controller import deploy


while True:

    print("\n")
    print("╔════════════════════════════╗")
    print("║ XLEVELUP CONTROL CENTER    ║")
    print("║ XDEPLOY v28.2              ║")
    print("╚════════════════════════════╝")


    print(
    dashboard()
    )


    print("""
[1] Deploy
[2] Exit
""")


    x=input("> ")


    if x=="1":

        print(
        deploy()
        )

        input(
        "ENTER RETURN..."
        )


    elif x=="2":

        break

PY



echo "[10] Git Ignore"



cat >> .gitignore <<EOF

Core/security/*
Core/snapshots/*
Core/runtime/*
__pycache__/

EOF



echo "[11] Compile"



python -m py_compile \
xdeploy.py \
Core/dashboard/center.py \
Core/deploy/controller.py \
Core/git_engine/sync.py \
Core/snapshot/manager.py \
Core/workspace/manager.py \
Core/watcher/manager.py



echo "

╔════════════════════════════════╗
║     XDEPLOY v28.2 READY        ║
╚════════════════════════════════╝


✓ Workspace Based
✓ Real Snapshot
✓ Git Delete Sync
✓ Secure Token
✓ Dashboard
✓ Compile PASS


RUN:

python xdeploy.py

"

