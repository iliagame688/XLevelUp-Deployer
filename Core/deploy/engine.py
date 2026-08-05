
import subprocess

from Core.git_engine.sync import sync
from Core.snapshot.manager import create



def deploy():


    snapshot=create()

    report=sync()


    subprocess.run(
    'git commit -m "XDEPLOY AUTO DEPLOY"',
    shell=True
    )


    push=subprocess.run(
    "git push origin main",
    shell=True
    )


    return {

    "deploy":
    "SUCCESS"
    if push.returncode==0
    else
    "FAILED",

    "snapshot":
    snapshot,

    "sync":
    report

    }

