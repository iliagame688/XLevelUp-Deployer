from rich.panel import Panel
from rich.table import Table



def header():

    return Panel(
        "[bold]XLEVELUP DEPLOYER v5[/bold]\n"
        "XDEPLOY MOBILE CONSOLE"
    )



def workspace(data):

    table = Table(
        expand=True
    )

    table.add_column(
        "FILES"
    )

    table.add_column(
        "VALUE"
    )


    table.add_row(
        "TOTAL",
        str(data.get("total",0))
    )

    table.add_row(
        "ADDED",
        str(data.get("added",0))
    )

    table.add_row(
        "DELETED",
        str(data.get("deleted",0))
    )


    return Panel(
        table,
        title="WORKSPACE"
    )



def services():

    return Panel(
        "Watcher  🟢\n"
        "Workspace 🟢\n"
        "Git       ⚪\n"
        "Recovery  🟢",
        title="SERVICES"
    )



def footer():

    return Panel(
        "XDEPLOY READY"
    )
