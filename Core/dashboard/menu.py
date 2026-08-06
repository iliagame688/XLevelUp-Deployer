from Core.v68.engine import deploy


AUTO=True


def run():

    global AUTO


    while True:

        print("""
╔══════════════════════════════════╗
║      XLEVELUP CONTROL CENTER     ║
║           XDEPLOY v68            ║
╚══════════════════════════════════╝


AUTO DEPLOY: %s


[1] Deploy Now
[2] Toggle Auto Deploy
[3] Events
[4] Exit

""" % ("ON" if AUTO else "OFF"))



        c=input("> ")


        if c=="1":

            print("""

╔════════════════════════════╗
║       XDEPLOY v68 REPORT    ║
╚════════════════════════════╝

""")


            print(
                deploy()
            )

            input(
                "\nENTER RETURN..."
            )


        elif c=="2":

            AUTO=not AUTO


        elif c=="3":

            print(
                "EVENT SYSTEM READY"
            )

            input(
                "\nENTER RETURN..."
            )


        elif c=="4":

            break

