
from pathlib import Path


class GitExecutor:


    def available(self, path="."):

        return Path(
            path,
            ".git"
        ).exists()



    def run(self, action, *args, **kwargs):


        path = kwargs.get(
            "path",
            "."
        )


        if not self.available(path):

            return {

                "status":
                    "SKIPPED",

                "mode":
                    "TEST",

                "action":
                    action,

                "message":
                    "Git repository missing"

            }



        return {

            "status":
                "READY",

            "action":
                action

        }



executor = GitExecutor()

