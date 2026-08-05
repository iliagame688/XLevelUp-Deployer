
import json

from pathlib import Path

from Core.vault.security import security



class VaultManager:


    def __init__(self):

        self.file = Path(
            "vault.json"
        )


    def save(self, data):


        safe = data.copy()


        if "token" in safe:

            safe["token_hash"] = (

                security.fingerprint(

                    safe["token"]

                )

            )

            safe["token"] = (

                security.mask(

                    safe["token"]

                )

            )


        self.file.write_text(

            json.dumps(

                safe,

                indent=4

            )

        )


        return True



    def load(self):


        if not self.file.exists():

            return None


        return json.loads(

            self.file.read_text()

        )




vault = VaultManager()

