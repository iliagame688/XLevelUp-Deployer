
import os


IGNORE=[

".git",

".xdeploy"

]


def scan(path):

    files=[]


    for root,dirs,fs in os.walk(path):

        dirs[:]=[
        d for d in dirs
        if d not in IGNORE
        ]


        for f in fs:

            files.append(
            os.path.relpath(
            os.path.join(root,f),
            path
            )
            )


    return files


