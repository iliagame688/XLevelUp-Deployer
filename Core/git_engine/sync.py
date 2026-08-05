
import subprocess



def run(cmd):

    return subprocess.run(
    cmd,
    shell=True,
    text=True,
    capture_output=True
    )



def sync(message="XDEPLOY AUTO SYNC"):


    run(
    "git add -A"
    )


    commit=run(
    f'git commit -m "{message}"'
    )


    push=run(
    "git push origin main"
    )


    return {


    "commit":
    commit.stdout,

    "push":
    push.stdout
    if push.returncode==0
    else
    push.stderr

    }

