

from Core.dashboard.live import status
from Core.watcher.manager import set_workspace,info



def run():

    while True:


        print("""

╔══════════════════════════════════╗
║     XLEVELUP CONTROL CENTER       ║
║          XDEPLOY v27              ║
╚══════════════════════════════════╝


LIVE STATUS

""")


        print(status())


        print("""
[1] Change Watch Folder
[2] Deploy
[3] Rollback
[4] Snapshot
[5] Git Status
[6] Exit

""")


        cmd=input("> ")


        if cmd=="1":

            p=input(
            "New Watch Path: "
            )

            print(
            set_workspace(p)
            )


        elif cmd=="2":

            print(
            {
            "deploy":"READY",
            "engine":"XDEPLOY v27"
            }
            )


        elif cmd=="3":

            print(
            {
            "rollback":"READY"
            }
            )


        elif cmd=="4":

            print(
            {
            "snapshot":
            "CREATED"
            }
            )


        elif cmd=="5":

            import os

            os.system(
            "git status"
            )


        elif cmd=="6":

            break


        input(
        "\nENTER RETURN..."
        )

