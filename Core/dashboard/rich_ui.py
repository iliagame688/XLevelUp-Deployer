from rich.console import Console

from rich.panel import Panel

from rich.table import Table

from rich.progress import (
    Progress,
    BarColumn,
    TextColumn
)

from Core.dashboard.widgets import status_icon



console = Console()



class RichDashboard:



    def engine_panel(
        self,
        engines
    ):


        table = Table(
            title="ENGINE STATUS"
        )


        table.add_column(
            "ENGINE"
        )


        table.add_column(
            "STATUS"
        )


        for name, data in engines.items():

            status = data.get(
                "status",
                "UNKNOWN"
            )


            table.add_row(

                name,

                f"{status_icon(status)} {status}"

            )


        console.print(
            Panel(table)
        )





    def live_feed(
        self,
        events
    ):


        text = ""


        for e in events[-8:]:

            text += (

                f'{e["time"]} '
                f'{e["operation"]} '
                f'{e["status"]}\n'

            )


        console.print(

            Panel(
                text,
                title="LIVE STREAM"
            )

        )





    def progress(
        self,
        value
    ):


        with Progress(

            TextColumn(
                "[progress.description]{task.description}"
            ),

            BarColumn()

        ) as progress:


            task = progress.add_task(

                "DEPLOY",

                total=100

            )


            progress.update(

                task,

                completed=value

            )





dashboard = RichDashboard()
