
import json
import os


FILE="Core/config/token.json"



def save(token):

    os.makedirs(
    "Core/config",
    exist_ok=True
    )

    json.dump(
    {
    "token":token
    },
    open(FILE,"w"),
    indent=4
    )


    return "TOKEN UPDATED"



def status():

    return os.path.exists(FILE)

