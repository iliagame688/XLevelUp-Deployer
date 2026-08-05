from pathlib import Path


class GitStatus:


    def check(self, path):

        git = Path(path) / ".git"


        return {

            "repository":

                git.exists(),

            "path":

                str(path)

        }




status = GitStatus()

