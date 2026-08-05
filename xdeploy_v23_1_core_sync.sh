#!/data/data/com.termux/files/usr/bin/bash

set -e

PROJECT="/storage/emulated/0/XLevelUp-Deployer"

cd "$PROJECT"


echo "
╔════════════════════════════════╗
║     XDEPLOY v23.1              ║
║       CORE SYNC PATCH          ║
╚════════════════════════════════╝
"


mkdir -p Core/dashboard


cat > Core/dashboard/center.py <<'PY'
from datetime import datetime


def dashboard():

    try:
        from Core.workspace.watcher import scan

        files=len(scan())

    except Exception:
        files=0


    return {

        "engine":"XDEPLOY v23.1",

        "status":"ONLINE",

        "time":str(datetime.now()),


        "workspace":{

            "files":files,

            "status":"WATCHING"

        },


        "modules":[

            "AI Brain",

            "Watcher",

            "Deploy",

            "Recovery",

            "Rollback",

            "Git Engine",

            "Control Plane"

        ],


        "server":{

            "status":"READY",

            "port":8080

        }

    }

PY



echo "[TEST] Dashboard"


python - <<'PY'

from Core.dashboard.center import dashboard

print(dashboard())

PY



python -m py_compile Core/dashboard/center.py


echo "

╔══════════════════════════════╗
║    XDEPLOY v23.1 READY       ║
╚══════════════════════════════╝


RUN:

python xdeploy.py

"

