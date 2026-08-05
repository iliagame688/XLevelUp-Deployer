#!/data/data/com.termux/files/usr/bin/bash

set -Eeuo pipefail


PROJECT="$(pwd)"

echo "
╔════════════════════════════════════╗
║        XDEPLOY v16                 ║
║     GIT CREDENTIAL BRIDGE          ║
╚════════════════════════════════════╝
"


mkdir -p Core/git_engine
mkdir -p Core/security
mkdir -p Core/events



echo "[1] Creating Auth Manager"


cat > Core/git_engine/auth.py <<'PY'
import json
import os


AUTH_FILE="Core/security/github_auth.json"


def load_auth():

    if not os.path.exists(AUTH_FILE):

        return {
            "status":"MISSING"
        }


    with open(AUTH_FILE) as f:

        data=json.load(f)


    return {
        "status":"ONLINE",
        "username":data.get("username"),
        "token":data.get("token")
    }



if __name__=="__main__":

    x=load_auth()

    print({

        "status":x["status"],

        "user":x.get("username"),

        "token":"LOADED" if x.get("token") else "NONE"

    })
PY



echo "[2] Creating Secret Firewall"


cat > Core/git_engine/guard.py <<'PY'
import os
import re


PATTERNS=[
    r"ghp_",
    r"github_pat_",
    r"BEGIN PRIVATE KEY",
    r"AKIA"
]


def scan():

    found=[]


    for root,dirs,files in os.walk("."):

        if ".git" in root:
            continue


        for f in files:

            if f.endswith(".py") or f.endswith(".json"):

                path=os.path.join(root,f)

                try:

                    data=open(
                        path,
                        errors="ignore"
                    ).read()


                    for p in PATTERNS:

                        if re.search(p,data):

                            found.append(path)

                            break


                except:
                    pass


    return found



if __name__=="__main__":

    print(scan())
PY



echo "[3] Creating Push Engine"


cat > Core/git_engine/push.py <<'PY'
import subprocess
import datetime

from Core.git_engine.auth import load_auth
from Core.git_engine.guard import scan


def run():

    auth=load_auth()


    if auth["status"]!="ONLINE":

        return {
            "status":"FAILED",
            "reason":"AUTH_MISSING"
        }



    secrets=scan()


    if secrets:

        return {

            "status":"BLOCKED",

            "reason":"SECRET_FOUND",

            "files":secrets

        }



    subprocess.run(
        [
            "git",
            "add",
            "."
        ]
    )


    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            "XDEPLOY v16 automated push"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


    result=subprocess.run(
        [
            "git",
            "push",
            "origin",
            "main"
        ],
        capture_output=True,
        text=True
    )


    return {

        "engine":"XDEPLOY v16",

        "status":
        "SUCCESS"
        if result.returncode==0
        else "FAILED",

        "time":
        str(datetime.datetime.now())

    }



if __name__=="__main__":

    print(run())
PY



echo "[4] Dashboard Bridge Test"


python - <<'PY'

from Core.git_engine.auth import load_auth
from Core.git_engine.guard import scan


print({

"AUTH":load_auth(),

"SECURITY_SCAN":scan()

})

PY



echo "[5] Git Setup"


git config --global credential.helper store



echo "
╔════════════════════════════════════╗
║       XDEPLOY v16 READY             ║
╚════════════════════════════════════╝


✓ AUTH BRIDGE CREATED
✓ SECRET FIREWALL ACTIVE
✓ PUSH ENGINE ONLINE
✓ DASHBOARD READY


TEST:

python -m Core.git_engine.push

"

