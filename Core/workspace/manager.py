import json
import os


CONFIG="Core/config/workspace.json"


def load():

    with open(CONFIG) as f:
        return json.load(f)



def set_workspace(path):

    data=load()

    data["workspace"]=path

    with open(CONFIG,"w") as f:
        json.dump(
            data,
            f,
            indent=4
        )

    return {
        "status":"UPDATED",
        "workspace":path
    }



def get_workspace():

    return load()["workspace"]


if __name__=="__main__":
    print(get_workspace())

