
from rich.console import Console
from rich.panel import Panel

from Core.dashboard.runtime_panel import runtime_panel
from Core.dashboard.intelligence import intelligence


console = Console()



def render():

    data = runtime_panel.snapshot()


    text = f"""

SYSTEM
━━━━━━━━━━━━━━━━
ENGINE       [✓ {data['ENGINE']}]
DASHBOARD    [✓ {data['DASHBOARD']}]
EVENT BUS    [✓ {data['EVENT_BUS']}]


DEPLOY
━━━━━━━━━━━━━━━━
MODE         [{data['DEPLOY_MODE']}]
STATUS       [{data['LAST_STATUS']}]


AI CORE
━━━━━━━━━━━━━━━━
ANALYZER     [✓ ONLINE]
MEMORY       [✓ READY]


REPAIR
━━━━━━━━━━━━━━━━
HEALTH       [✓ READY]
RECOVERY     [✓ READY]


SECURITY
━━━━━━━━━━━━━━━━
VAULT        [WAITING]
AUTH         [NOT REQUIRED]

"""


    console.print(
        Panel.fit(
            text,
            title="XLEVELUP COMMAND CENTER"
        )
    )


def render_intelligence():

    data = intelligence.snapshot()


    print()

    print(
        "╭──────── XLEVELUP INTELLIGENCE ────────╮"
    )


    if data:

        print(
            f"SESSION     {data.get('session','-')}"
        )

        print(
            f"TIME        {data.get('time','-')}"
        )

        print()

        print(
            f"ENGINE      {data.get('engine','-')}"
        )

        print(
            f"MODE        {data.get('mode','-')}"
        )

        print()

        print(
            "MODULES"
        )


        for name,status in data.get(
            "modules",
            {}
        ).items():

            print(
                f"✓ {name:<10} {status}"
            )


        print()

        deploy = data.get(
            "deploy",
            {}
        )


        print(
            "DEPLOY"
        )

        print(
            f"STATUS      {deploy.get('status','-')}"
        )

        print(
            f"STEPS       {deploy.get('steps',0)}"
        )


    else:

        print(
            "INTELLIGENCE WAITING"
        )


    print(
        "╰────────────────────────────────────────╯"
    )

