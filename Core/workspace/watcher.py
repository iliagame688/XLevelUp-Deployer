import os
import time
from .manager import load


def scan():

    cfg=load()

    root=cfg["workspace"]

    ignore=cfg["ignore"]

    files=[]

    for base,dirs,names in os.walk(root):

        dirs[:]=[
            d for d in dirs
            if d not in ignore
        ]

        for n in names:

            path=os.path.join(base,n)

            if not any(
                x in path
                for x in ignore
            ):
                files.append(path)

    return files



def watch():

    old=set(scan())

    print(
        "WATCHING:",
        len(old),
        "files"
    )


    while True:

        time.sleep(2)

        new=set(scan())

        added=list(new-old)

        removed=list(old-new)


        if added:
            print(
                "ADDED",
                added
            )


        if removed:
            print(
                "REMOVED",
                removed
            )


        old=new



if __name__=="__main__":
    watch()

