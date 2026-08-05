
import json
import os


FILE="Core/runtime/state.json"



def save(data):

    os.makedirs(
        "Core/runtime",
        exist_ok=True
    )


    with open(FILE,"w") as f:

        json.dump(
            data,
            f,
            indent=4
        )



def load():

    if os.path.exists(FILE):

        return json.load(
            open(FILE)
        )

    return {}

