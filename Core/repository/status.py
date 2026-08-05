
class RepositoryStatus:


    def __init__(self):

        self.data = {

            "repo":
                None,

            "mode":
                None,

            "remote":
                None

        }


    def update(self, value):

        self.data.update(value)


    def get(self):

        return self.data




status = RepositoryStatus()

