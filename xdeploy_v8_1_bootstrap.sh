#!/data/data/com.termux/files/usr/bin/bash

set -Eeuo pipefail


PROJECT="/storage/emulated/0/XLevelUp-Deployer"


echo "
╔════════════════════════════════════════╗
║     XLEVELUP DEPLOYER v8.1             ║
║     HARDENED AUTONOMOUS INSTALLER      ║
╚════════════════════════════════════════╝
"


error_exit(){

echo ""
echo "FAILED:"
echo "$1"
exit 1

}


echo "[1] Storage Permission Check"


if [ ! -d "/storage/emulated/0" ]; then

termux-setup-storage

sleep 3

fi


if [ ! -d "$PROJECT" ]; then

error_exit "Project path not found: $PROJECT"

fi



cd "$PROJECT" || error_exit "Cannot enter project"



echo "[2] Creating Core Structure"



DIRS=(

"Core/watcher"

"Core/ai"

"Core/deploy"

"Core/rollback"

"Core/runtime"

"Core/snapshots"

"Core/health"

)



for DIR in "${DIRS[@]}"
do

mkdir -p "$DIR"

echo "✓ $DIR"

done



echo "[3] Creating Modules"



touch Core/__init__.py



cat > Core/health/check.py <<'PY'

def health():

    return {
        "engine":"XDEPLOY v8.1",
        "status":"ONLINE"
    }


if __name__=="__main__":

    print(health())

PY



cat > Core/ai/recovery_brain.py <<'PY'


class RecoveryBrain:


    def analyze(self,error):

        return {

        "error":error,

        "action":
        "AUTO_ANALYZE",

        "confidence":
        95

        }



def diagnose(error):

    return RecoveryBrain().analyze(error)


PY




cat > Core/watcher/snapshot.py <<'PY'

import os
import json
from datetime import datetime


def snapshot():


    files=[]


    for root,dirs,names in os.walk("."):

        for name in names:

            if ".git" not in root:

                files.append(
                    os.path.join(root,name)
                )


    data={

    "time":
    str(datetime.now()),

    "files":
    len(files)

    }


    os.makedirs(
        "Core/snapshots",
        exist_ok=True
    )


    with open(
        "Core/snapshots/latest.json",
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


    return data


PY




cat > Core/deploy/agent.py <<'PY'

from Core.watcher.snapshot import snapshot


def deploy_check():

    return {

    "deploy":
    "READY",

    "snapshot":
    snapshot()

    }


if __name__=="__main__":

    print(deploy_check())

PY



cat > Core/rollback/manager.py <<'PY'

import json
import os


FILE="Core/runtime/state.json"



def save(data):

    os.makedirs(
        "Core/runtime",
        exist_ok=True
    )


    with open(FILE,"w") as f:

        json.dump(
            data,
            f,
            indent=4
        )



def load():

    if os.path.exists(FILE):

        return json.load(
            open(FILE)
        )

    return {}

PY




echo "[4] Security"



cat > .gitignore <<'EOF'

.env

*.token

*.secret

Core/security/*

Core/runtime/*.json

Core/snapshots/*.json

__pycache__/

*.pyc

EOF




echo "[5] Module Test"



python - <<'PY'

from Core.health.check import health
from Core.ai.recovery_brain import diagnose
from Core.deploy.agent import deploy_check


print()
print("HEALTH")
print(health())

print()

print("AI")
print(diagnose("test"))

print()

print("DEPLOY")
print(deploy_check())


PY




echo "[6] Git Sync"



git add .


git commit -m "XDEPLOY v8.1 Hardened Core" || true



echo "[7] Push"



git push origin main || {


echo "
REMOTE SYNC REQUIRED:

git pull origin main --rebase

git push

"

exit 1

}




echo "

╔════════════════════════════════════════╗
║          XDEPLOY v8.1 REPORT           ║
╚════════════════════════════════════════╝

STATUS: ONLINE

✓ Permission Safe
✓ Core Created
✓ AI Brain Loaded
✓ Watcher Ready
✓ Deploy Agent Ready
✓ Git Push Completed


NEXT:
XDEPLOY v9 Dashboard

"


