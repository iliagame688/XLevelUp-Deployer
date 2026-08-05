from rich.panel import Panel
from rich.table import Table



def core_page():

    table = Table(
        show_header=False
    )


    table.add_row(
        "ENGINE",
        "🟢 RUNNING"
    )

    table.add_row(
        "CORE",
        "🟢 READY"
    )

    table.add_row(
        "INTELLIGENCE",
        "🟢 ACTIVE"
    )


    return Panel(
        table,
        title="CORE STATUS"
    )




def project_page():

    table = Table(
        show_header=False
    )


    table.add_row(
        "WORKSPACE",
        "CONNECTED"
    )

    table.add_row(
        "FILES",
        "AUTO DETECT"
    )

    table.add_row(
        "STRUCTURE",
        "HEALTHY"
    )


    return Panel(
        table,
        title="PROJECT"
    )





def deploy_page():

    table = Table(
        show_header=False
    )


    table.add_row(
        "QUEUE",
        "READY"
    )


    table.add_row(
        "ENGINE",
        "ONLINE"
    )


    return Panel(
        table,
        title="DEPLOY"
    )





def intelligence_page():

    table = Table(
        show_header=False
    )


    table.add_row(
        "DIAGNOSIS",
        "READY"
    )


    table.add_row(
        "HISTORY",
        "ACTIVE"
    )


    return Panel(
        table,
        title="INTELLIGENCE"
    )
