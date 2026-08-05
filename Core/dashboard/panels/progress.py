from rich.panel import Panel
from rich.progress_bar import ProgressBar


def render(value):


    bar = ProgressBar(
        total=100,
        completed=value
    )


    return Panel(

        bar,

        title=f"DEPLOY {value}%"

    )
