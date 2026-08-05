from Core.navigator.menu import menu


class Router:



    def open(
        self,
        target=None
    ):


        if target:

            if target in menu.items:

                menu.index = menu.items.index(
                    target
                )


        return {

            "active":
                menu.current(),

            "available":
                menu.items

        }




router = Router()
