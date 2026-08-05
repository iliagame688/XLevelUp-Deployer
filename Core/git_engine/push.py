import subprocess
import datetime

from Core.git_engine.auth import load_auth
from Core.git_engine.guard import scan


def run():

    auth=load_auth()


    if auth["status"]!="ONLINE":

        return {
            "status":"FAILED",
            "reason":"AUTH_MISSING"
        }



    secrets=scan()


    if secrets:

        return {

            "status":"BLOCKED",

            "reason":"SECRET_FOUND",

            "files":secrets

        }



    subprocess.run(
        [
            "git",
            "add",
            "."
        ]
    )


    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            "XDEPLOY v16 automated push"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


    result=subprocess.run(
        [
            "git",
            "push",
            "origin",
            "main"
        ],
        capture_output=True,
        text=True
    )


    return {

        "engine":"XDEPLOY v16",

        "status":
        "SUCCESS"
        if result.returncode==0
        else "FAILED",

        "time":
        str(datetime.datetime.now())

    }



if __name__=="__main__":

    print(run())
