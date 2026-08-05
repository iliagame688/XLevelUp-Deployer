from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.console import Console

import time

from Core.control.screen import device



console = Console()



def header():

    return Panel(
        "XLEVELUP CONTROL CENTER v6\nZERO TERMUX EDITION",
        title="XCONTROL"
    )



def status():

    table = Table(
        show_header=False,
        expand=True
    )


    table.add_row(
        "CORE",
        "🟢 ONLINE"
    )

    table.add_row(
        "ENGINE",
        "🟢 READY"
    )

    table.add_row(
        "INTELLIGENCE",
        "🟢 ACTIVE"
    )


    return Panel(
        table,
        title="SYSTEM"
    )



def modules():

    table = Table(
        show_header=False
    )


    table.add_row(
        "GIT",
        "🟡 READY"
    )


    table.add_row(
        "DEPLOY",
        "🟢 READY"
    )


    table.add_row(
        "WATCHER",
        "🟢 ACTIVE"
    )


    return Panel(
        table,
        title="MODULES"
    )



def info():

    data = device()


    return Panel(
        f"""
Platform:
{data["platform"]}

Python:
{data["python"]}
""",
        title="DEVICE"
    )



def build():

    layout = Layout()


    layout.split_column(

        Layout(
            header(),
            size=5
        ),

        Layout(
            name="main"
        )

    )


    layout["main"].split_row(

        Layout(
            status()
        ),

        Layout(
            modules()
        ),

        Layout(
            info()
        )

    )


    return layout




def launch():

    with Live(
        build(),
        refresh_per_second=1,
        screen=True
    ) as live:


        while True:

            live.update(
                build()
            )

            time.sleep(1)



if __name__ == "__main__":

    launch()
