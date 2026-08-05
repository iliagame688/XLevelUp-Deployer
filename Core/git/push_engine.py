from Core.git.gateway import gateway
from Core.git.safe import safe_git


# GIT SAFE MODE

from pathlib import Path


def git_available(path="."):

    return (
        Path(path, ".git").exists()
    )


import subprocess
import json

from pathlib import Path
from datetime import datetime


HISTORY = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/push_history.json"
)



def save_history(data):

    items = []

    if HISTORY.exists():

        try:
            items = json.loads(
                HISTORY.read_text(
                    encoding="utf-8"
                )
            )
        except:
            items = []


    data["time"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    items.append(data)


    HISTORY.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    HISTORY.write_text(
        json.dumps(
            items,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )



class PushEngine:


    def check_git(self, path):

        return safe_git(path)


    def remote(self, path):


        check = self.check_git(path)

        if not check["allowed"]:

            return ""



        try:

            result = subprocess.check_output(
                [
                    "git",
                    "-C",
                    path,
                    "remote",
                    "-v"
                ],
                text=True
            )

            return result.strip()


        except Exception as e:

            return ""



    def branch(self, path):

        try:

            return subprocess.check_output(
                [
                    "git",
                    "-C",
                    path,
                    "branch",
                    "--show-current"
                ],
                text=True
            ).strip()


        except:

            return "UNKNOWN"



    def push(self, path):


        check = self.check_git(path)


        if not check["allowed"]:

            return {

                "action":
                    "PUSH",

                "status":
                    "SKIPPED",

                "mode":
                    "TEST",

                "reason":
                    "GIT_REPOSITORY_MISSING"

            }



        data = {

            "action":
                "PUSH",

            "branch":
                self.branch(path)

        }


        remote = self.remote(path)


        if not remote:

            data.update({

                "status":
                    "FAILED",

                "reason":
                    "NO_REMOTE"

            })

            save_history(data)

            return data



        try:

            subprocess.check_call(

                [
                    "git",
                    "-C",
                    path,
                    "push"
                ]

            )


            data.update({

                "status":
                    "SUCCESS",

                "remote":
                    remote

            })


        except Exception as e:


            error = str(e)


            if "permission" in error.lower():

                reason = "PERMISSION_ERROR"

            elif "auth" in error.lower():

                reason = "AUTH_ERROR"

            else:

                reason = "PUSH_ERROR"



            data.update({

                "status":
                    "FAILED",

                "reason":
                    reason,

                "error":
                    error

            })



        save_history(data)


        return data



push_engine = PushEngine()
