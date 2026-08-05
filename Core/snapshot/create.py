
import os
import shutil
import datetime


IGNORE=[
".git"
]


def create(path):

    name=datetime.datetime.now().strftime(
    "%Y%m%d_%H%M%S"
    )


    target="Core/snapshots/"+name


    os.makedirs(
    target,
    exist_ok=True
    )


    for x in os.listdir(path):

        if x in IGNORE:
            continue


        src=os.path.join(path,x)

        dst=os.path.join(target,x)


        if os.path.isdir(src):

            shutil.copytree(
            src,
            dst
            )

        else:

            shutil.copy2(
            src,
            dst
            )


    return target

