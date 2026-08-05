from rich.panel import Panel
from rich.table import Table



def system_panel(data):

    table = Table(
        show_header=False,
        box=None
    )

    table.add_row(
        "CORE",
        data.get(
            "core",
            "UNKNOWN"
        )
    )

    table.add_row(
        "ENGINE",
        data.get(
            "engine",
            "UNKNOWN"
        )
    )

    table.add_row(
        "INTELLIGENCE",
        data.get(
            "intelligence",
            "UNKNOWN"
        )
    )


    return Panel(
        table,
        title="SYSTEM"
    )





def project_panel(data):

    table = Table(
        show_header=False,
        box=None
    )


    table.add_row(
        "FILES",
        str(
            data.get(
                "files",
                0
            )
        )
    )


    table.add_row(
        "STATUS",
        data.get(
            "status",
            "UNKNOWN"
        )
    )


    return Panel(
        table,
        title="PROJECT"
    )





def connection_panel(data):

    table = Table(
        show_header=False,
        box=None
    )


    table.add_row(
        "GITHUB",
        data.get(
            "github",
            "WAITING"
        )
    )


    table.add_row(
        "TOKEN",
        data.get(
            "token",
            "WAITING"
        )
    )


    return Panel(
        table,
        title="CONNECTIONS"
    )
