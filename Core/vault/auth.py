
import json
from pathlib import Path



class AuthVault:


    def __init__(self):

        self.file = Path(

            "Core/vault/.auth.json"

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



    def exists(self):


        return self.file.exists()




vault = AuthVault()

