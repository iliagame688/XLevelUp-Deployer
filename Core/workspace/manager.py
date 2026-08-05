
import json
import os


ROOT=os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


FILE=os.path.join(
    ROOT,
    "config",
    "system.json"
)



def load():

    if not os.path.exists(FILE):

        return {
        "engine":"XDEPLOY v33.2",
        "workspace":"",
        "repo":"",
        "branch":"main"
        }


    with open(FILE) as f:

        return json.load(f)



def save(data):

    os.makedirs(
    os.path.dirname(FILE),
    exist_ok=True
    )


    with open(FILE,"w") as f:

        json.dump(
        data,
        f,
        indent=4
        )



def set_workspace(path):

    data=load()

    data["workspace"]=os.path.abspath(path)

    save(data)

    return data



def get_workspace():

    return load().get(
        "workspace",
        ""
    )

