from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout

from dashboard.collector import collect



def make_panel(title, rows):

    table = Table(
        show_header=False,
        expand=True
    )

    table.add_column(
        "KEY"
    )

    table.add_column(
        "VALUE"
    )


    for k, v in rows:

        table.add_row(
            k,
            str(v)
        )


    return Panel(
        table,
        title=title
    )



def render():


    data = collect()


    layout = Layout()


    layout.split_column(

        Layout(
            name="top",
            size=7
        ),

        Layout(
            name="middle"
        ),

        Layout(
            name="bottom",
            size=8
        )
    )



    layout["middle"].split_row(

        Layout(
            name="left"
        ),

        Layout(
            name="right"
        )

    )



    layout["top"].update(

        Panel(
            "[bold]XLEVELUP DEPLOYER v5[/bold]\n"
            "MOBILE DEPLOY CONSOLE",
            title="XDEPLOY"
        )

    )



    ws = data["workspace"]


    layout["left"].update(

        make_panel(
            "WORKSPACE",

            [

                (
                "STATUS",
                "🟢 CONNECTED"
                ),

                (
                "FILES",
                ws["total"]
                ),

                (
                "ADDED",
                ws["added"]
                ),

                (
                "MODIFIED",
                ws["modified"]
                ),

                (
                "DELETED",
                ws["deleted"]
                )

            ]
        )

    )



    layout["right"].update(

        make_panel(
            "SERVICES",

            [

                (
                "WATCHER",
                "🟢 RUNNING"
                ),

                (
                "GIT",
                data["git"]["status"]
                ),

                (
                "RECOVERY",
                data["recovery"]["state"]
                )

            ]

        )

    )



    layout["bottom"].update(

        Panel(

            "LIVE EVENTS\n"
            "Waiting for events...",

            title="STREAM"

        )

    )


    return layout


def show_runtime(runtime):

    print()

    print(
        "╭──────── XLEVELUP RUNTIME STATUS ────────╮"
    )

    for name, data in runtime.items():

        if isinstance(data, dict):

            status = data.get(
                "status",
                "-"
            )

            print(
                f"{name:<12} | {status}"
            )

        else:

            print(
                f"{name:<12} | {data}"
            )


    print(
        "╰──────────────────────────────────────────╯"
    )





def render_runtime(result):

    try:

        runtime = result.get(
            "dashboard",
            {}
        ).get(
            "runtime",
            {}
        )

        show_runtime(
            runtime
        )

    except Exception as e:

        print(
            "Runtime Render Error:",
            e
        )


def render_runtime_metrics(state):

    runtime = state.get(
        "runtime",
        {}
    )

    if not runtime:
        return


    print()

    print(
        "╭──────── XLEVELUP RUNTIME METRICS ────────╮"
    )


    for name, data in runtime.items():

        if isinstance(data, dict):

            status = data.get(
                "status",
                "-"
            )

            extra = []

            for k,v in data.items():

                if k != "status":
                    extra.append(
                        f"{k}={v}"
                    )

            info = " ".join(extra)

            print(
                f"{name:<12} | {status} {info}"
            )

        else:

            print(
                f"{name:<12} | {data}"
            )


    print(
        "╰──────────────────────────────────────────╯"
    )

