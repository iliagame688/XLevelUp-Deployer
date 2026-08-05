
import os


def scan():

    count=0

    for root,dirs,files in os.walk("."):

        if ".git" not in root:

            count += len(files)


    return {

    "files":count,

    "watcher":"ACTIVE"

    }


