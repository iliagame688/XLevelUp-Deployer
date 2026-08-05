
from Core.dashboard.control_plane import (
    dashboard,
    deploy,
    rollback
)


print("""

╔══════════════════════════════╗
║     XLEVELUP LIVE CENTER      ║
║        XDEPLOY v17            ║
╚══════════════════════════════╝

""")


print("[STATUS]")
print(
    dashboard()["center"]
)


print("\n[COMMANDS]")
print("1 - DEPLOY")
print("2 - ROLLBACK")
print("3 - EVENTS")


cmd=input("> ")


if cmd=="1":

    print(
        deploy()
    )


elif cmd=="2":

    print(
        rollback()
    )


elif cmd=="3":

    print(
        dashboard()["events"]
    )

