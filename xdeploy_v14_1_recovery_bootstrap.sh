#!/data/data/com.termux/files/usr/bin/bash

set -e


PROJECT="/storage/emulated/0/XLevelUp-Deployer"

cd "$PROJECT"


echo "
╔════════════════════════════════════╗
║       XDEPLOY v14.1                ║
║     PIPELINE RECOVERY ENGINE       ║
╚════════════════════════════════════╝
"



mkdir -p Core/recovery


echo "[1] Creating Syntax Recovery"



cat > Core/recovery/pipeline_guard.py <<'PY'

import os
import ast
import shutil
import datetime



BROKEN=[]



def check_file(path):

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            ast.parse(
                f.read()
            )


        return True


    except Exception as e:


        BROKEN.append({

            "file":path,

            "error":str(e)

        })


        return False




def scan(root="."):


    BROKEN.clear()


    for base,dirs,files in os.walk(root):


        if ".git" in base:
            continue


        for file in files:


            if file.endswith(".py"):

                check_file(
                os.path.join(
                base,
                file
                )
                )



    return BROKEN




def quarantine(path):


    if os.path.exists(path):

        backup=path+".broken_"+datetime.datetime.now().strftime(
            "%H%M%S"
        )


        shutil.move(
            path,
            backup
        )


        return backup



    return None



PY




echo "[2] Creating Safe Preflight"



cat > Core/pipeline/safe_preflight.py <<'PY'


from Core.recovery.pipeline_guard import scan


def run():


    errors=scan()


    if errors:


        return {

        "status":"BLOCKED",

        "reason":"SYNTAX_ERRORS",

        "errors":errors

        }



    return {


    "status":"READY",

    "reason":"CLEAN"


    }


PY




echo "[3] Testing"



python - <<'PY'

from Core.pipeline.safe_preflight import run

print(
run()
)

PY



echo "
╔════════════════════════════════════╗
║    XDEPLOY v14.1 READY              ║
╚════════════════════════════════════╝


NEXT:

Repair broken deploy.py

"

