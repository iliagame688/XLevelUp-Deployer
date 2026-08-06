
import os
import subprocess
import datetime


from Core.config.manager import get_workspace



ENGINE_ROOT=os.path.abspath(
os.path.join(
os.path.dirname(__file__),
"../.."
)
)



PROTECTED=[

ENGINE_ROOT,

os.path.join(
ENGINE_ROOT,
"Core"
),

os.path.join(
ENGINE_ROOT,
"xdeploy.py"
)

]



def deploy():


    workspace=get_workspace()



    if not workspace:

        return {
        "status":"FAILED",
        "reason":"NO_WORKSPACE"
        }



    workspace=os.path.abspath(workspace)



    if workspace in PROTECTED:

        return {
        "status":"BLOCKED",
        "reason":"ENGINE_PATH"
        }



    if not os.path.exists(
    workspace
    ):

        return {
        "status":"FAILED",
        "reason":"WORKSPACE_NOT_FOUND"
        }



    os.chdir(workspace)



    subprocess.run(
    "git add -A",
    shell=True
    )


    commit=subprocess.run(
    'git commit -m "XDEPLOY AUTO MIRROR"',
    shell=True,
    capture_output=True,
    text=True
    )


    push=subprocess.run(
from Core.git.smart_push import smart_push

push_result = smart_push()

    shell=True,
    capture_output=True,
    text=True
    )


    return {

    "status":
    "DEPLOYED",

    "workspace":
    workspace,

    "commit":
    commit.stdout,

    "push":
    push.stdout

    }

