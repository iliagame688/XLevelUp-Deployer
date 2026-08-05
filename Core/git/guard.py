
from pathlib import Path
import subprocess



class GitGuard:


    def check(self, path):


        git_dir = Path(path) / ".git"


        if git_dir.exists():

            return {

                "status":
                    "READY",

                "message":
                    "Git repository detected"

            }



        return {

            "status":
                "MISSING",

            "message":
                "Git repository not initialized",

            "suggestion":
                "Run git init"

        }




guard = GitGuard()

