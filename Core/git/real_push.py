import subprocess
from Core.git.auth import auth


ROOT="/storage/emulated/0/XLevelUp-Deployer"


def real_push():


    token = auth.authenticate()


    remote = (
        "https://"
        "iliagame688:"
        +
        token
        +
        "@github.com/"
        "iliagame688/"
        "XLevelUp-Deployer.git"
    )


    subprocess.run(
        [
            "git",
            "remote",
            "set-url",
            "origin",
            remote
        ],
        cwd=ROOT
    )


    result = subprocess.run(
        [
            "git",
            "push",
            "--set-upstream",
            "origin",
            "main"
        ],
        cwd=ROOT,
        capture_output=True,
        text=True
    )


    if result.returncode != 0:

        return {

            "status":
                "PUSH_FAILED",

            "error":
                result.stderr

        }



    return {

        "status":
            "PUSH_SUCCESS",

        "message":
            "DEPLOY COMPLETE"

    }
