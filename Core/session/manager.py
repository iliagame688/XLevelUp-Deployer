
import json
from pathlib import Path


class SessionManager:


    def __init__(self):

        self.file = Path(
            "session.json"
        )


    def save(self, data):

        self.file.write_text(

            json.dumps(

                data,

                indent=4

            )

        )


    def load(self):

        if not self.file.exists():

            return None


        return json.loads(

            self.file.read_text()

        )


    def clear(self):

        if self.file.exists():

            self.file.unlink()



session = SessionManager()

