import os
import subprocess


def sh(cmd):

    return subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )


def prepare(repo_path,remote=None):

    os.makedirs(
        repo_path,
        exist_ok=True
    )

    os.chdir(repo_path)


    if not os.path.exists(".git"):

        sh("git init")


    sh(
    'git config user.name "XDEPLOY-AI"'
    )

    sh(
    'git config user.email "xdeploy@local.engine"'
    )


    if remote:

        r=sh(
        "git remote"
        )

        if "origin" not in r.stdout:

            sh(
            f"git remote add origin {remote}"
            )


def status():

    return sh(
    "git status --short"
    ).stdout



def deploy():

    sh(
    "git add -A"
    )

    s=status()


    if not s:

        return {
        "git":"CLEAN"
        }


    c=sh(
    'git commit -m "XDEPLOY v42 AUTO SYNC"'
    )


    p=sh(
    "git push origin main"
    )


    return {

    "commit":
    c.stdout or c.stderr,

    "push":
    p.stdout or p.stderr

    }

