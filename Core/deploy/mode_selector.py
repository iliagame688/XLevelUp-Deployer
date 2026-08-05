
from pathlib import Path
import json


FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/deploy_mode.json"
)



class DeployMode:


    def get(self):

        if not FILE.exists():

            return "TEST"


        try:

            return json.loads(
                FILE.read_text()
            ).get(
                "mode",
                "TEST"
            )

        except:

            return "TEST"



    def set(self,value):

        FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        FILE.write_text(
            json.dumps(
                {
                    "mode":value
                },
                indent=4
            )
        )

        return value



mode = DeployMode()
