import json
import os


CONFIG="Core/config/workspace.json"


def get_workspace():

    with open(CONFIG) as f:

        return json.load(f)



def set_workspace(path):

    data={
        "path":os.path.abspath(path),
        "watch":True,
        "auto_snapshot":True
    }


    with open(CONFIG,"w") as f:

        json.dump(
            data,
            f,
            indent=4
        )


    return data

