import os
import shutil
from datetime import datetime


IMPORT = "from Core.git.push_router import push_router"


TARGETS = [
    "git push",
    "['git','push']",
    '["git","push"]',
    "git\",\"push",
    "git', 'push"
]


def backup(file):

    b = (
        file +
        ".backup_" +
        datetime.now().strftime("%H%M%S")
    )

    shutil.copy(file,b)

    print("BACKUP:",b)



def patch(file):

    try:
        data=open(file).read()
    except:
        return


    if "push_router()" in data:
        return


    found=False

    for x in TARGETS:

        if x in data:
            found=True


    if not found:
        return



    backup(file)



    lines=data.splitlines()

    out=[]

    inserted=False


    for line in lines:


        if any(x in line for x in TARGETS):

            if not inserted:

                out.append(
                    IMPORT
                )

                out.append(
                    ""
                )

                out.append(
                    "push_result = push_router()"
                )

                inserted=True

            continue



        out.append(line)



    open(file,"w").write(
        "\n".join(out)
    )


    print(
        "PATCHED:",
        file
    )





for root,dirs,files in os.walk("."):


    dirs[:]=[
        d for d in dirs
        if "backup" not in d
    ]


    for f in files:

        if f.endswith(".py"):

            patch(
                os.path.join(root,f)
            )



print()
print(
"⚡ XDEPLOY SMART PUSH BRIDGE CONNECTED"
)

