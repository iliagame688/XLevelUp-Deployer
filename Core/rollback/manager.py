

import json
import os


STATE="Core/runtime/state.json"


def save(data):

    os.makedirs(
    "Core/runtime",
    exist_ok=True
    )


    json.dump(
    data,
    open(STATE,"w"),
    indent=4
    )



def load():

    if os.path.exists(STATE):

        return json.load(
        open(STATE)
        )

    return {}

