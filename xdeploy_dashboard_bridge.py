import os
import shutil
from datetime import datetime


MAIN="xdeploy.py"

NEW_IMPORT="from Core.dashboard.v87.pro_center import run"

OLD_IMPORTS=[
    "from Core.dashboard.menu import run",
    "from Core.dashboard.v86.rich_events import run",
    "from Core.dashboard.v87.control_center import run"
]


def backup():

    if os.path.exists(MAIN):

        name=f"{MAIN}.backup_{datetime.now().strftime('%H%M%S')}"

        shutil.copy(
            MAIN,
            name
        )

        print(
            "BACKUP:",
            name
        )



def patch():

    if not os.path.exists(MAIN):

        print(
            "xdeploy.py not found"
        )

        return


    with open(
        MAIN,
        "r"
    ) as f:

        data=f.read()



    changed=False


    for old in OLD_IMPORTS:

        if old in data:

            data=data.replace(
                old,
                NEW_IMPORT
            )

            changed=True



    if NEW_IMPORT not in data:

        data=NEW_IMPORT+"\n"+data

        changed=True



    with open(
        MAIN,
        "w"
    ) as f:

        f.write(data)



    if changed:

        print(
            "XDEPLOY DASHBOARD BRIDGE CONNECTED"
        )

    else:

        print(
            "ALREADY CONNECTED"
        )




if __name__=="__main__":

    backup()
    patch()

