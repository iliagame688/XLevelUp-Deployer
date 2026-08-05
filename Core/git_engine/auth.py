import json
import os


AUTH_FILE="Core/security/github_auth.json"


def load_auth():

    if not os.path.exists(AUTH_FILE):

        return {
            "status":"MISSING"
        }


    with open(AUTH_FILE) as f:

        data=json.load(f)


    return {
        "status":"ONLINE",
        "username":data.get("username"),
        "token":data.get("token")
    }



if __name__=="__main__":

    x=load_auth()

    print({

        "status":x["status"],

        "user":x.get("username"),

        "token":"LOADED" if x.get("token") else "NONE"

    })
