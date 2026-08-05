import json
import os


CONFIG="Core/config/system.json"


def load():

    with open(CONFIG) as f:
        return json.load(f)



def save(data):

    with open(CONFIG,"w") as f:
        json.dump(
            data,
            f,
            indent=4
        )



def set_workspace(path):

    data=load()

    data["workspace"]=os.path.abspath(path)

    save(data)

    return {
        "workspace":
        data["workspace"]
    }



def get_workspace():

    return load().get(
        "workspace",
        ""
    )
