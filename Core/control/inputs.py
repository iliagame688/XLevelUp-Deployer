from rich.console import Console
from rich.panel import Panel

from Core.control.validator import validator



console = Console()



def token_input():


    token = console.input(
        "\n[bold]GitHub Token:[/bold] "
    )


    result = validator.token(
        token
    )


    if result["valid"]:

        console.print(
            Panel(
                "🟢 TOKEN VALID\n\n"
                + result["reason"],
                title="SUCCESS"
            )
        )

    else:

        console.print(
            Panel(
                "🔴 TOKEN INVALID\n\n"
                + result["reason"],
                title="ERROR"
            )
        )


    return result
