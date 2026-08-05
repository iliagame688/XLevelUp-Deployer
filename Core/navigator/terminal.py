from Core.navigator.menu import menu


class TerminalNavigator:



    def show(self):


        print(

            "\n╭──── XCONTROL MENU ────╮"

        )


        for i,item in enumerate(
            menu.items
        ):


            pointer = ">" if i == menu.index else " "


            print(
                pointer,
                item
            )


        print(
            "╰──────────────────────╯"
        )



navigator = TerminalNavigator()
