class Menu:


    def __init__(self):

        self.items = [

            "HOME",
            "WORKSPACE",
            "GIT",
            "DEPLOY",
            "LOGS",
            "SETTINGS"

        ]

        self.index = 0



    def current(self):

        return self.items[
            self.index
        ]



    def next(self):

        self.index += 1


        if self.index >= len(self.items):

            self.index = 0


        return self.current()



    def previous(self):

        self.index -= 1


        if self.index < 0:

            self.index = len(self.items)-1


        return self.current()




menu = Menu()
