from rich.table import Table
from rich.panel import Panel



def create_status_panel(data):

    table = Table(
        show_header=False
    )


    table.add_row(
        "CORE",
        data["CORE"]
    )


    table.add_row(
        "INTELLIGENCE",
        data["INTELLIGENCE"]
    )


    project = data["PROJECT"]


    table.add_row(
        "FILES",
        str(
            project["files"]
        )
    )


    github = data["GITHUB"]


    table.add_row(
        "GITHUB",
        github["status"]
    )


    table.add_row(
        "ACCOUNT",
        github["account"]
    )


    return Panel(
        table,
        title="XCONTROL LIVE STATUS"
    )
