import json
from pathlib import Path
from datetime import datetime


STATE_FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/runtime_state.json"
)


STATES = [

    "IDLE",
    "WATCHING",
    "CHANGES_FOUND",
    "SYNCING",
    "DEPLOYING",
    "VERIFIED",
    "ERROR"

]



def default_state():

    return {

        "state":
            "IDLE",

        "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "events":
            0,

        "last_action":
            "START"

    }




def load_state():

    if not STATE_FILE.exists():

        return default_state()


    try:

        return json.loads(
            STATE_FILE.read_text(
                encoding="utf-8"
            )
        )

    except:

        return default_state()




def save_state(data):

    STATE_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    STATE_FILE.write_text(

        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ),

        encoding="utf-8"
    )




def set_state(new_state, action=""):


    if new_state not in STATES:

        return False



    data = load_state()


    data["state"] = new_state

    data["last_action"] = action

    data["time"] = (
        datetime.now()
        .strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )


    save_state(data)


    return True




def register_event():

    data = load_state()

    data["events"] += 1


    if data["events"] > 0:

        data["state"] = (
            "CHANGES_FOUND"
        )


    save_state(data)



def status():

    return load_state()



if __name__ == "__main__":

    print(status())
