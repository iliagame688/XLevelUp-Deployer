from Core.git.gateway import gateway


# GIT SAFE MODE

from pathlib import Path


def git_available(path="."):

    return (
        Path(path, ".git").exists()
    )


import subprocess

from Core.upload.commit import (
    generate_message
)



class CommitEngine:



    def run(
        self,
        path,
        files
    ):


        if not files:

            return {

                "status":
                    "NO_CHANGES",

                "message":
                    "Nothing to commit"

            }



        try:


            subprocess.check_call(

                [
                    "git",
                    "-C",
                    path,
                    "add"
                ]
                +
                files

            )



            message = generate_message(
                files
            )



            subprocess.check_call(

                [
                    "git",
                    "-C",
                    path,
                    "commit",
                    "-m",
                    message
                ]

            )



            return {

                "status":
                    "SUCCESS",

                "commit":
                    message,

                "files":
                    files

            }



        except Exception as e:


            return {

                "status":
                    "FAILED",

                "error":
                    str(e)

            }



commit_engine = CommitEngine()
