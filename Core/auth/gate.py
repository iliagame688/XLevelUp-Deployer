
from pathlib import Path
import json


class AuthGate:


    def check(self):

        files = [

            "vault.json",
            "credentials.json",
            "Core/data/github.json"

        ]


        for f in files:

            if Path(f).exists():

                try:

                    data = json.loads(
                        Path(f).read_text()
                    )

                    if data:

                        return {

                            "auth": True,
                            "source": f

                        }

                except:

                    pass


        return {

            "auth": False,
            "source": None

        }



gate = AuthGate()
