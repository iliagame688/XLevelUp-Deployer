from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

from Core.control.panels import (
    system_panel,
    project_panel,
    connection_panel
)



console = Console()



def launch(context=None):

    context = context or {}


    layout = Layout()


    layout.split_column(

        Layout(
            name="header",
            size=3
        ),

        Layout(
            name="body"
        )

    )


    layout["header"].update(
        Panel(
            "XLEVELUP CONTROL CENTER v1",
            title="XCONTROL"
        )
    )


    body = Layout()


    body.split_row(

        Layout(
            system_panel(
                context
            )
        ),

        Layout(
            project_panel(
                context
            )
        )

    )


    layout["body"].update(
        body
    )


    console.print(layout)

    console.print(
        connection_panel(
            context
        )
    )
