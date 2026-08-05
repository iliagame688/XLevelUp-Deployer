import os
import json


FILE=os.path.expanduser(
"~/.xdeploy/vault.json"
)



def save(token):

    os.makedirs(
        os.path.dirname(FILE),
        exist_ok=True
    )

    with open(FILE,"w") as f:

        json.dump(
            {
             "github_token":token
            },
            f
        )


    return {
    "status":"SAVED"
    }



def load():

    if not os.path.exists(FILE):

        return None


    with open(FILE) as f:

        return json.load(f)
