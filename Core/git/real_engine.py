
import subprocess
from pathlib import Path


class RealGitEngine:


    def cmd(self,args,path):

        return subprocess.run(
            ["git","-C",str(path)] + args,
            capture_output=True,
            text=True
        )


    def init(self,path):

        git = Path(path)/".git"

        if not git.exists():

            self.cmd(
                ["init"],
                path
            )

        self.cmd(
            [
                "branch",
                "-M",
                "main"
            ],
            path
        )


        return True



    def remote(self,path,url):

        check = self.cmd(
            [
                "remote"
            ],
            path
        )


        if "origin" not in check.stdout:

            self.cmd(
                [
                    "remote",
                    "add",
                    "origin",
                    url
                ],
                path
            )


        return True



    def upload(self,path,message):

        self.cmd(
            [
                "add",
                "."
            ],
            path
        )


        commit = self.cmd(
            [
                "commit",
                "-m",
                message
            ],
            path
        )


        push = self.cmd(
            [
                "push",
                "-u",
                "origin",
                "main"
            ],
            path
        )


        return {

            "commit":
                commit.stdout + commit.stderr,

            "push":
                push.stdout + push.stderr,

            "status":
                "SUCCESS"
                if push.returncode == 0
                else "FAILED"

        }



real_git = RealGitEngine()
