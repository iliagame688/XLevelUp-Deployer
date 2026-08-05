from pathlib import Path
import subprocess


class GitControl:


    def check(self, path="."):

        return Path(
            path,
            ".git"
        ).exists()



    def execute(self, path, command):

        if not self.check(path):

            return {

                "status":
                    "SKIPPED",

                "mode":
                    "TEST",

                "reason":
                    "NO_GIT_REPOSITORY",

                "command":
                    command

            }


        try:

            result = subprocess.run(
                ["git","-C",path] + command,
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

                "status":
                    "FAILED",

                "error":
                    str(e)

            }



git_control = GitControl()

