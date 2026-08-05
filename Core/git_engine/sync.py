import subprocess


def execute(cmd):

    return subprocess.run(
        cmd,
        shell=True,
        text=True,
        capture_output=True
    )



def sync(message):


    add=execute(
        "git add -A"
    )


    commit=execute(
        f'git commit -m "{message}"'
    )


    push=execute(
        "git push origin main"
    )


    return {

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
