#!/data/data/com.termux/files/usr/bin/bash

set -e


echo "
╔════════════════════════════════════╗
║     XDEPLOY v16.1                  ║
║     FIREWALL PATCH                 ║
╚════════════════════════════════════╝
"


cat > Core/git_engine/guard.py <<'PY'
import os
import re


IGNORE=[
    ".git",
    "__pycache__",
    "Core/runtime",
    "Core/archive",
    "github_auth.json",
    ".env"
]


PATTERNS=[
    r"ghp_[A-Za-z0-9]+",
    r"github_pat_[A-Za-z0-9_]+",
    r"BEGIN PRIVATE KEY",
    r"AKIA[0-9A-Z]+"
]


def ignored(path):

    for x in IGNORE:

        if x in path:

            return True

    return False



def scan():

    found=[]


    for root,dirs,files in os.walk("."):


        if ignored(root):

            dirs[:]=[]

            continue



        for file in files:


            path=os.path.join(root,file)


            if ignored(path):

                continue



            if not file.endswith(
                (".py",".json",".sh",".txt")
            ):

                continue



            try:

                data=open(
                    path,
                    errors="ignore"
                ).read()



                for pattern in PATTERNS:

                    if re.search(
                        pattern,
                        data
                    ):

                        found.append(path)

                        break


            except:

                pass



    return found



if __name__=="__main__":

    print(scan())

PY



echo "[TEST] Firewall"


python - <<'PY'

from Core.git_engine.guard import scan

print({
"SECURITY_STATUS":
"PASS"
if not scan()
else "BLOCKED",

"FILES":
scan()

})

PY



echo "
XDEPLOY v16.1 PATCH COMPLETE
"

