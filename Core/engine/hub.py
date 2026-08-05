import json
from pathlib import Path
from datetime import datetime


from Core.engine.registry import (
    register,
    update,
    all_services
)

from Core.engine.health import check



STATE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/engine.json"
)



class Engine:


    def __init__(self):

        register(
            "CORE",
            "RUNNING"
        )


    def register(self, name):

        register(
            name
        )



    def update(self, name, status):

        update(
            name,
            status
        )



    def snapshot(self):

        data = {

            "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),


            "services":
            all_services(),


            "health":
            check()

        }


        STATE.write_text(

            json.dumps(
                data,
                indent=4,
                ensure_ascii=False
            ),

            encoding="utf-8"

        )


        return data




engine = Engine()
