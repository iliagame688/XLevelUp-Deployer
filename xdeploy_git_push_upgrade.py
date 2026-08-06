import os
import shutil
from datetime import datetime


IMPORT_LINE = "from Core.git.push_router import push_router"


def backup(path):

    backup = (
        path +
        ".backup_push_" +
        datetime.now().strftime("%H%M%S")
    )

    shutil.copy(path, backup)

    print(
        "[BACKUP]",
        backup
    )



def patch_file(path):

    try:

        with open(path,"r") as f:
            data=f.read()


    except:
        return



    if "git push" not in data:
        return



    if "push_router" in data:
        return



    backup(path)



    lines=data.splitlines()

    output=[]

    injected=False


    for line in lines:


        # subprocess git push
        if (
            "git push" in line
            or
            '"push"' in line
            or
            "'push'" in line
        ):


            if not injected:

                output.append(
                    IMPORT_LINE
                )

                output.append(
                    ""
                )

                output.append(
                    "push_result = push_router()"
                )

                output.append(
                    ""
                )

                injected=True


            continue



        output.append(line)



    if injected:

        with open(path,"w") as f:

            f.write(
                "\n".join(output)
            )


        print(
            "[PATCHED]",
            path
        )





for root,dirs,files in os.walk("."):


    # ignore backups
    dirs[:] = [
        d for d in dirs
        if "backup" not in d
    ]


    for file in files:


        if file.endswith(".py"):

            patch_file(
                os.path.join(
                    root,
                    file
                )
            )



print()
print(
"⚡ XDEPLOY SMART PUSH UPGRADE COMPLETE"
)

