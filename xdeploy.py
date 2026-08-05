
import os


from Core.config.config import load,set_value

from Core.deploy.mirror import deploy



def menu():


    while True:


        os.system("clear")


        print("""
╔══════════════════════════════════╗
║     XLEVELUP CONTROL CENTER      ║
║          XDEPLOY v35             ║
╚══════════════════════════════════╝
""")


        print(
        load()
        )


        print("""
[1] Workspace
[2] Repo
[3] Deploy
[4] Exit
""")


        c=input("> ")


        if c=="1":

            print(
            set_value(
            "workspace",
            input("PATH: ")
            )
            )


        elif c=="2":

            print(
            set_value(
            "repo",
            input("REPO URL: ")
            )
            )


        elif c=="3":

            print(
            deploy()
            )


        elif c=="4":

            break


        input(
        "ENTER RETURN..."
        )



if __name__=="__main__":

    menu()

