import os
import json


CONFIG_FILE="Core/config/workspace.json"


DEFAULT={
    "path":"/storage/emulated/0/XLevelUp-Deployer",
    "ignore":[
        ".git",
        "__pycache__",
        "Core/runtime",
        "Core/archive"
    ]
}


def load_workspace():

    os.makedirs(
        "Core/config",
        exist_ok=True
    )


    if not os.path.exists(CONFIG_FILE):

        save_workspace(DEFAULT)
        return DEFAULT


    with open(CONFIG_FILE) as f:
        data=json.load(f)



    # OLD VERSION SUPPORT

    if "path" not in data:

        if "watch_path" in data:
            data["path"]=data["watch_path"]

        elif "workspace" in data:
            data["path"]=data["workspace"]

        else:
            data["path"]=DEFAULT["path"]



    if "ignore" not in data:
        data["ignore"]=DEFAULT["ignore"]


    save_workspace(data)

    return data



def save_workspace(data):

    with open(CONFIG_FILE,"w") as f:
        json.dump(
            data,
            f,
            indent=4
        )


def set_workspace(path):

    cfg=load_workspace()

    cfg["path"]=path

    save_workspace(cfg)

    return cfg
