
import os
import json


PATH=os.path.expanduser(
"~/.xdeploy/token.json"
)



def save(token):

    os.makedirs(
    os.path.dirname(PATH),
    exist_ok=True
    )


    with open(PATH,"w") as f:

        json.dump(
        {
        "token":token
        },
        f
        )


    return "TOKEN SAVED"



def load():

    if not os.path.exists(PATH):
        return None


    with open(PATH) as f:

        return json.load(f)

