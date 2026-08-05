import os
import json
import time

from Core.workspace.manager import get_workspace


IGNORE=[
".git",
"Core/runtime",
"Core/snapshots",
"__pycache__"
]


CACHE="Core/data/watch.json"


def scan():

    root=get_workspace()

    if not root or not os.path.exists(root):

        return []


    files=[]


    for base,dirs,names in os.walk(root):

        dirs[:]=[
            d for d in dirs
            if d not in IGNORE
        ]


        for name in names:

            path=os.path.join(
                base,
                name
            )

            files.append(path)


    return files



def state():

    files=scan()

    data={

    "files":
    len(files),

    "workspace":
    get_workspace(),

    "status":
    "WATCHING"

    }


    with open(
        CACHE,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


    return data



def watch():

    old=set(scan())


    while True:

        time.sleep(3)

        new=set(scan())


        added=list(
            new-old
        )

        deleted=list(
            old-new
        )


        if added or deleted:

            print(
            {
            "ADDED":added,
            "DELETED":deleted
            }
            )


        old=new
