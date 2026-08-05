
class GitHubStatus:


    def __init__(self):

        self.state = {

            "connected":
                False,

            "account":
                None,

            "auth":
                None

        }


    def update(self, data):

        self.state.update(data)


    def get(self):

        return self.state




status = GitHubStatus()

