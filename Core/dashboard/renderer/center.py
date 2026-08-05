from rich.layout import Layout

from Core.dashboard.panels import (
    status,
    deploy,
    ai
)


from Core.dashboard.live.stream import stream

from Core.dashboard.panels.live import live_panel



def build():


    layout = Layout(
        name="root"
    )


    layout.split_column(

        Layout(
            name="top",
            size=3
        ),

        Layout(
            name="body"
        ),

        Layout(
            name="bottom",
            size=8
        )

    )


    layout["body"].split_row(

        Layout(
            name="left"
        ),

        Layout(
            name="right"
        )

    )


    layout["top"].update(

        "╭──── XCONTROL CENTER ────╮"

    )


    layout["left"].update(

        status.render()

    )


    layout["right"].update(

        ai.render()

    )


    layout["bottom"].update(

        live_panel(
            stream.latest()
        )

    )


    return layout
