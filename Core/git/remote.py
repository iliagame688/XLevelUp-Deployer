
import subprocess


def run(cmd):

    return subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )



def setup(repo):


    current=run(
        "git remote get-url origin"
    )


    if current.returncode != 0:


        run(
            f"git remote add origin {repo}"
        )


    else:


        url=current.stdout.strip()


        if url != repo:

            run(
            f"git remote set-url origin {repo}"
            )



    return run(
        "git remote -v"
    ).stdout


