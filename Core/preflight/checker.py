
from pathlib import Path
import os


class PreflightChecker:


    def check(self, path, config=None):


        result = {

            "workspace": False,

            "git": False,

            "auth": False,

            "mode": "REAL",

            "warnings": []

        }



        # Workspace

        if Path(path).exists():

            result["workspace"] = True

        else:

            result["warnings"].append(
                "Workspace missing"
            )



        # Git

        if Path(path, ".git").exists():

            result["git"] = True

        else:

            result["warnings"].append(
                "Git repository missing - TEST MODE"
            )



        # Auth

        if config:

            auth = config.get(
                "auth"
            )

            if auth:

                result["auth"] = True



        # Mode

        if (
            result["workspace"]
            and result["auth"]
        ):

            result["mode"] = "READY"



        return result




checker = PreflightChecker()

