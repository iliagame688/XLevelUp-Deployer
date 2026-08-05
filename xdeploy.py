
from Core.dashboard.center import dashboard

from Core.deploy.controller import deploy


while True:

    print("\n")
    print("╔════════════════════════════╗")
    print("║ XLEVELUP CONTROL CENTER    ║")
    print("║ XDEPLOY v28.2              ║")
    print("╚════════════════════════════╝")


    print(
    dashboard()
    )


    print("""
[1] Deploy
[2] Exit
""")


    x=input("> ")


    if x=="1":

        print(
        deploy()
        )

        input(
        "ENTER RETURN..."
        )


    elif x=="2":

        break

