from pathlib import Path
import subprocess


class GitGateway:


    def __init__(self):

        self.mode = "TEST"



    def check(self, path):

        if Path(path, ".git").exists():

            self.mode = "REAL"

            return True

        self.mode = "TEST"

        return False



    def run(self, path, args):

        if not self.check(path):

            return {

                "status":"SKIPPED",

                "mode":"TEST",

                "reason":"NO_GIT_REPOSITORY",

                "command":args

            }



        try:

            result = subprocess.run(
                ["git","-C",path] + args,
                capture_output=True,
                text=True
            )


            return {

                "status":
                    "SUCCESS"
                    if result.returncode == 0
                    else "FAILED",

                "stdout":
                    result.stdout,

                "stderr":
                    result.stderr

            }


        except Exception as e:


            return {

                "status":"FAILED",

                "error":str(e)

            }



gateway = GitGateway()
