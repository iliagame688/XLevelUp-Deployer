
from pathlib import Path
import subprocess


class SmartGitGuard:


    def check(self, path):

        root = Path(path)

        result = {

            "git": False,
            "initialized": False,
            "remote": False,
            "branch": None,
            "mode": "SAFE"

        }


        git = root / ".git"


        if git.exists():

            result["git"] = True
            result["initialized"] = True


            try:

                branch = subprocess.check_output(
                    [
                        "git",
                        "-C",
                        str(root),
                        "branch",
                        "--show-current"
                    ],
                    text=True
                ).strip()


                result["branch"] = branch


            except:

                pass


            try:

                remote = subprocess.check_output(
                    [
                        "git",
                        "-C",
                        str(root),
                        "remote"
                    ],
                    text=True
                ).strip()


                if remote:

                    result["remote"] = True


            except:

                pass



        else:

            result["warning"] = (
                "GIT NOT INITIALIZED"
            )


        return result



guard = SmartGitGuard()
