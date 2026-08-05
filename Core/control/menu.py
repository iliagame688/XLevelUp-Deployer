from Core.deploy.executor import deploy
from Core.deploy.preflight import scan
from Core.snapshot.manager import create
from Core.events.live import get_events


def git_status():

    import subprocess

    try:

        out=subprocess.check_output(
            ["git","status","--short"]
        ).decode()

        return {

        "git":"ONLINE",

        "changes":out.splitlines()

        }


    except Exception as e:

        return {

        "git":"ERROR",

        "error":str(e)

        }



def show():

    print("""
╔══════════════════════════════════╗
║     XLEVELUP CONTROL CENTER      ║
║          XDEPLOY v26             ║
╚══════════════════════════════════╝


[1] AI Deploy
[2] AI Scan
[3] Snapshot
[4] Rollback
[5] Git Status
[6] Events
[7] Exit

""")


    while True:


        choice=input("> ")



        if choice=="1":

            print("\n[AI DEPLOY]\n")

            print(
            deploy()
            )



        elif choice=="2":

            print("\n[AI SCAN]\n")

            print(
            scan()
            )



        elif choice=="3":

            print("\n[SNAPSHOT]\n")

            print(
            create()
            )



        elif choice=="4":

            print({

            "rollback":"READY",

            "engine":"XDEPLOY v26"

            })



        elif choice=="5":

            print(
            git_status()
            )



        elif choice=="6":

            print(
            get_events()
            )



        elif choice=="7":

            print(
            "EXIT XDEPLOY"
            )

            break


        else:

            print(
            "INVALID COMMAND"
            )


