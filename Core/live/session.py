import json

from pathlib import Path
from datetime import datetime


FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/live_session.json"
)



class SessionManager:


    def __init__(self):

        self.items = []



    def add(
        self,
        name,
        status,
        detail=""
    ):

        item = {

            "time":
                datetime.now().strftime(
                    "%H:%M:%S"
                ),

            "operation":
                name,

            "status":
                status,

            "detail":
                detail

        }


        self.items.append(item)

        self.save()

        return item



    def save(self):

        FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        FILE.write_text(

            json.dumps(
                self.items,
                indent=4,
                ensure_ascii=False
            ),

            encoding="utf-8"

        )



    def history(self):

        return self.items



session = SessionManager()
