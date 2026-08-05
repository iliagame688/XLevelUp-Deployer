class CommandRegistry:


    def __init__(self):

        self.commands = {}



    def register(
        self,
        name,
        action
    ):

        self.commands[name] = action



    def get(
        self,
        name
    ):

        return self.commands.get(
            name
        )



    def list(self):

        return list(
            self.commands.keys()
        )



registry = CommandRegistry()
