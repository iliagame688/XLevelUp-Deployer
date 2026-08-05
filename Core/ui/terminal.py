import os
from Core.control.actions import deploy_action,rollback_action
from Core.events.stream import get_events
from Core.dashboard.center import dashboard


def clear():
    os.system("clear")


def start():

    while True:

        clear()

        print("""
╔══════════════════════════════════╗
║     XLEVELUP CONTROL CENTER      ║
║          XDEPLOY v23             ║
╚══════════════════════════════════╝
        """)


        print("\nSTATUS")
        print(dashboard())


        print("""
        
[1] Deploy
[2] Rollback
[3] Events
[4] Exit

        """)


        cmd=input("> ")


        if cmd=="1":
            print(deploy_action())
            input()


        elif cmd=="2":
            print(rollback_action())
            input()


        elif cmd=="3":
            print(get_events())
            input()


        elif cmd=="4":
            break

