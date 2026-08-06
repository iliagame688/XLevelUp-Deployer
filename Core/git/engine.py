from Core.git.deploy import deploy



class GitEngine:


    def __init__(self,repo):

        self.repo=repo



    def run(self):

        return deploy(
            self.repo
        )
