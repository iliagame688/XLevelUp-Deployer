
import os
import json


PATH=os.path.expanduser(
"~/.xdeploy/vault.json"
)



def set_token(token):

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


    return {
    "token":
    "SAVED"
    }



def status():

    return {

    "vault":
    os.path.exists(PATH)

    }

