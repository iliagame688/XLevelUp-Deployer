
from Core.dashboard.live.live_console import live_console
from Core.preflight.checker import checker
from Core.preflight.renderer import renderer


from Core.bridge.deploy_bridge import bridge
from Core.deploy.commands import is_real
from Core.deploy.bridge_real import run_real
from Core.deploy.router import dispatch
from Core.dashboard.kernel import kernel
from Core.git.smart_guard import guard
from Core.auth.gate import gate
from Core.dashboard.live.dashboard_stream import dashboard



def start():

    kernel.boot()

    # LIVE DASHBOARD BOOT
    live_console


    workspace = "/storage/emulated/0/XLevelUp-Deployer"


    preflight = checker.check(
        workspace,
        {}
    )


    renderer.show(
        preflight
    )


    print(
        "\n⚡ STARTING SAFE DEPLOY MODE..."
    )


    workspace = (

        "/storage/emulated/0/"

        "XLevelUp-Deployer"

    )


    config = {

        "mode":

            "REAL",

        "real":

            True

    }



    result = dispatch(

        workspace

    )


    print()


    dashboard.render()

    print(

        "⚡ ENGINE ONLINE"

    )




    print()

    print(
        "╭──────── XLEVELUP DEPLOY REPORT ────────╮"
    )

    try:

        print()

        print(
            "ENGINE:",
            result.get(
                "engine",
                "XDEPLOY"
            )
        )


        final = result.get(
            "final",
            result
        )


        print(
            "STATUS:",
            final.get(
                "status",
                result.get(
                    "status",
                    "UNKNOWN"
                )
            )
        )


        print(
            "MODE:",
            final.get(
                "mode",
                result.get(
                    "mode",
                    "REAL"
                )
            )
        )


        print()

        for step in result.get(
            "steps",
            []
        ):

            print(
                "✓",
                step.get(
                    "name",
                    "-"
                )
            )


        if result.get("error"):

            print()

            print(
                "ERROR:",
                result.get("error")
            )


    except Exception as e:

        print(
            "REPORT ERROR:",
            e
        )


    print(
        "╰──────────────────────────────────────╯"
    )


    return result



