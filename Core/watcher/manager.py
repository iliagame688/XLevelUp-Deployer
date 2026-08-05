
import os

from Core.workspace.manager import get_workspace



IGNORE=[
".git",
"Core/runtime",
"Core/snapshots",
"__pycache__"
]


def scan():

    cfg=get_workspace()

    root=cfg["path"]

    result=[]


    for base,dirs,files in os.walk(root):

        dirs[:]=[
            d for d in dirs
            if d not in IGNORE
        ]


        for file in files:

            path=os.path.join(
                base,
                file
            )

            result.append(path)


    return result



def status():

    return {

    "workspace":
    get_workspace()["path"],

    "files":
    len(scan()),

    "status":
    "WATCHING"

    }

