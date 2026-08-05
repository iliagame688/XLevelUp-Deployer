
import os
import json
from datetime import datetime


def snapshot():


    files=[]


    for root,dirs,names in os.walk("."):

        for name in names:

            if ".git" not in root:

                files.append(
                    os.path.join(root,name)
                )


    data={

    "time":
    str(datetime.now()),

    "files":
    len(files)

    }


    os.makedirs(
        "Core/snapshots",
        exist_ok=True
    )


    with open(
        "Core/snapshots/latest.json",
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


    return data


