class GitAuth:


    def __init__(self):

        self.connected = False



    def check(self):

        return {

            "authenticated":
                self.connected

        }



    def set_connected(self):

        self.connected = True




auth = GitAuth()
