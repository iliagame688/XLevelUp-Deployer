

import os


from Core.dashboard.live import show

from Core.config.settings import update

from Core.security.vault import set_token,status



def clear():

    os.system("clear")



def run():

    while True:


        clear()


        print("""
╔══════════════════════════════════╗
║     XLEVELUP CONTROL CENTER      ║
║          XDEPLOY v32             ║
╚══════════════════════════════════╝
""")


        print(
        show()
        )


        print("""

[1] Change Workspace
[2] Set Repo
[3] Set Branch
[4] Token Settings
[5] Exit

""")


        cmd=input("> ")



        if cmd=="1":

            p=input(
            "Workspace: "
            )

            print(
            update(
            "workspace",
            p
            )
            )


        elif cmd=="2":

            r=input(
            "Repository: "
            )

            print(
            update(
            "repo",
            r
            )
            )


        elif cmd=="3":

            b=input(
            "Branch: "
            )

            print(
            update(
            "branch",
            b
            )
            )


        elif cmd=="4":

            t=input(
            "Git Token: "
            )

            print(
            set_token(t)
            )

            print(
            status()
            )


        elif cmd=="5":

            break


        input(
        "ENTER RETURN..."
        )



# XDEPLOY v33 AUTO

from Core/deploy.auto import deploy


