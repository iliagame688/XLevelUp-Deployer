class TabManager:


    def __init__(self):

        self.tabs = [

            "HOME",
            "WORKSPACE",
            "GIT",
            "DEPLOY",
            "LOGS",
            "SETTINGS"

        ]



    def list(self):

        return self.tabs



    def open(self, name):

        if name in self.tabs:

            return {

                "tab":
                    name,

                "status":
                    "ACTIVE"

            }


        return {

            "tab":
                name,

            "status":
                "NOT_FOUND"

        }




tabs = TabManager()
