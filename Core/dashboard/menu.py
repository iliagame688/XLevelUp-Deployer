
import os

from Core.dashboard.center import status

from Core.deploy.engine import deploy

from Core.workspace.manager import set_workspace

from Core.security.token import save

from Core.recovery.rollback import rollback



def clear():

    os.system("clear")



def run():

    while True:

        clear()

        print("""
╔══════════════════════════════════╗
║      XLEVELUP CONTROL CENTER      ║
║          XDEPLOY v30              ║
╚══════════════════════════════════╝
""")

        print("LIVE STATUS")
        print(status())


        print("""
[1] Change Workspace
[2] Deploy
[3] Rollback
[4] Token Settings
[5] Exit
""")


        cmd=input("> ")



        if cmd=="1":

            path=input(
            "Workspace Path: "
            )

            print(
            set_workspace(path)
            )


            input(
            "ENTER RETURN..."
            )


        elif cmd=="2":

            print(
            deploy()
            )

            input(
            "ENTER RETURN..."
            )


        elif cmd=="3":

            print(
            rollback()
            )

            input(
            "ENTER RETURN..."
            )


        elif cmd=="4":

            token=input(
            "GitHub Token: "
            )

            print(
            save(token)
            )

            input(
            "ENTER RETURN..."
            )


        elif cmd=="5":

            break

