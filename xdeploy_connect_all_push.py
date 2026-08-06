import os
import shutil
from datetime import datetime


IMPORT = "from Core.git.push_router import push_router"


TARGETS = [
    "git push origin",
    "git push",
]


IGNORE = [
    ".backup",
    "archive",
    "snapshots",
    "__pycache__"
]



def backup(path):

    b = path + ".backup_smartpush_" + datetime.now().strftime("%H%M%S")

    shutil.copy(
        path,
        b
    )



def patch(path):

    try:
        data=open(path).read()
    except:
        return


    if "push_router()" in data:
        return


    if not any(x in data for x in TARGETS):
        return


    if any(x in path for x in IGNORE):
        return



    backup(path)


    lines=data.splitlines()

    out=[]

    added=False


    for line in lines:


        if "git push" in line:


            if not added:

                out.append(
                    IMPORT
                )

                out.append(
                    ""
                )

                out.append(
                    "push_result = push_router()"
                )

                out.append(
                    ""
                )

                added=True


            continue



        out.append(line)



    if added:

        with open(path,"w") as f:

            f.write(
                "\n".join(out)
            )


        print(
            "PATCHED:",
            path
        )





for root,dirs,files in os.walk("."):


    dirs[:] = [
        d for d in dirs
        if not any(
            x in d
            for x in IGNORE
        )
    ]


    for f in files:

        if f.endswith(".py"):

            patch(
                os.path.join(root,f)
            )


print()
print(
"⚡ XDEPLOY ALL ACTIVE PUSH ENGINES UPGRADED"
)

