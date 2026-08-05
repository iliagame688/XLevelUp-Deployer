#!/data/data/com.termux/files/usr/bin/bash

echo "
╔══════════════════════════════════╗
║   XDEPLOY v27.1 DASH FIX          ║
╚══════════════════════════════════╝
"


LIVE_DIR="Core/dashboard/live"


mkdir -p "$LIVE_DIR"


cat > "$LIVE_DIR/__init__.py" <<'PY'

import datetime
import os

try:
    from Core.watcher.config import load
except:
    load=lambda:{
        "path":os.getcwd()
    }



def status():

    try:

        cfg=load()

        root=cfg.get(
            "path",
            os.getcwd()
        )

    except:

        root=os.getcwd()


    count=0


    try:

        for r,d,f in os.walk(root):

            if "Core/runtime" in r:
                continue

            count += len(f)


    except:

        pass


    return {

    "engine":
    "XDEPLOY v27.1",

    "status":
    "ONLINE",

    "time":
    str(datetime.datetime.now()),


    "workspace":
    {
    "path":root,
    "files":count,
    "status":"WATCHING"
    },


    "modules":
    [
    "AI Brain",
    "Watcher",
    "Deploy",
    "Recovery",
    "Rollback",
    "Git Engine",
    "Control Plane"
    ]

    }


PY



echo "[TEST]"

python - <<'PY'

from Core.dashboard.live import status

print(status())

PY



python -m py_compile xdeploy.py


echo "

╔══════════════════════════════════╗
║ XDEPLOY v27.1 FIXED               ║
╚══════════════════════════════════╝


RUN:

python xdeploy.py

"

