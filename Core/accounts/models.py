class GitAccount:


    def __init__(
        self,
        name
    ):

        self.name = name

        self.authenticated = False

        self.workspaces = []



    def status(self):

        return {

            "name":
                self.name,

            "auth":
                self.authenticated,

            "workspaces":
                self.workspaces

        }
