
import subprocess
import os


def run(cmd):

    return subprocess.run(
        cmd,
        cwd=WORKSPACE,
        shell=True,
        text=True,
        capture_output=True
    )



from Core.workspace.manager import get_workspace


WORKSPACE=""


def sync(message):

    global WORKSPACE


    WORKSPACE=get_workspace()


    if not WORKSPACE:

        return {
        "status":"FAILED",
        "reason":"NO_WORKSPACE"
        }


    if not os.path.exists(
        os.path.join(WORKSPACE,".git")
    ):

        return {
        "status":"FAILED",
        "reason":"NO_GIT_REPOSITORY"
        }



    add=run(
    "git add -A"
    )


    commit=run(
    f'git commit -m "{message}"'
    )


    push=run(
    "git push origin main"
    )


    return {

    "workspace":
    WORKSPACE,

    "add":
    add.returncode==0,

    "commit":
    commit.stdout,

    "push":
    push.stdout
    if push.returncode==0
    else
    push.stderr

    }

