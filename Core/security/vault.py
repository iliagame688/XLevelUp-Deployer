
import os
import json


VAULT=os.path.expanduser(
"~/.xdeploy/vault.json"
)


def save_token(token):

    os.makedirs(
    os.path.dirname(VAULT),
    exist_ok=True
    )

    with open(VAULT,"w") as f:

        json.dump(
        {
        "github_token":token
        },
        f
        )


    return {
    "status":"SAVED"
    }



def load_token():

    if not os.path.exists(VAULT):

        return None


    with open(VAULT) as f:

        return json.load(f)

