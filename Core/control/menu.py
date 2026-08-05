from rich.console import Console

from Core.control.pages import (
    core_page,
    project_page,
    deploy_page,
    intelligence_page
)



console = Console()



def show():

    while True:


        console.clear()


        console.print(
            """
╭──────── XCONTROL ────────╮
│ XLEVELUP COMMAND CENTER  │
╰──────────────────────────╯


[1] Core Engine

[2] Project

[3] Deploy

[4] Intelligence

[0] Exit
"""
        )


        choice = console.input(
            "Select > "
        )



        console.clear()


        if choice == "1":

            console.print(
                core_page()
            )


        elif choice == "2":

            console.print(
                project_page()
            )


        elif choice == "3":

            console.print(
                deploy_page()
            )


        elif choice == "4":

            console.print(
                intelligence_page()
            )


        elif choice == "0":

            break


        console.input(
            "\nPress ENTER..."
        )
