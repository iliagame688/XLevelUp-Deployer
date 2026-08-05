
import json
import os


FILE="Core/config/workspace.json"


DEFAULT={
"path":os.getcwd()
}


def load():

    if not os.path.exists(FILE):

        save(DEFAULT)
        return DEFAULT

    return json.load(open(FILE))


def save(data):

    os.makedirs(
        "Core/config",
        exist_ok=True
    )

    json.dump(
        data,
        open(FILE,"w"),
        indent=4
    )

