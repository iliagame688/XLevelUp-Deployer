from Core.git.gateway import gateway
from Core.git.safe import safe_git
import subprocess

from Core.git.history import add



class GitActions:


    def status(self, path):

        try:

            output = subprocess.check_output(
                [
                    "git",
                    "-C",
                    path,
                    "status",
                    "--short"
                ],
                text=True
            )


            files = [
                x.strip()
                for x in output.splitlines()
                if x.strip()
            ]


            result = {

                "repo":
                    True,

                "changed":
                    files,

                "count":
                    len(files)

            }


        except Exception as e:

            result = {

                "repo":
                    False,

                "error":
                    str(e)

            }


        add({

            "action":
                "GIT_STATUS",

            "result":
                result

        })


        return result





    def branch(self, path):

        try:

            branch = subprocess.check_output(
                [
                    "git",
                    "-C",
                    path,
                    "branch",
                    "--show-current"
                ],
                text=True
            ).strip()


            return branch


        except:

            return "UNKNOWN"



git_actions = GitActions()
