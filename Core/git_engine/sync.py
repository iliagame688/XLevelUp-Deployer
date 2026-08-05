
import subprocess
import datetime


IGNORE=[
"Core/security/",
"Core/runtime/",
"Core/snapshots/",
"__pycache__/",
".xdeploy/"
]


def run(c):

    return subprocess.check_output(
    c,
    shell=True,
    text=True
    ).strip()



def scan():

    out=run(
    "git status --short"
    )

    result=[]


    for x in out.splitlines():

        if not x:
            continue


        file=x[3:]


        if any(
        file.startswith(i)
        for i in IGNORE
        ):
            continue


        result.append(
        {
        "state":x[:2].strip(),
        "file":file
        }
        )


    return result




def sync():

    changes=scan()


    subprocess.run(
    "git add -A",
    shell=True
    )


    return {

    "engine":"XDEPLOY v28",

    "time":
    str(datetime.datetime.now()),

    "changes":
    changes,

    "count":
    len(changes)

    }

