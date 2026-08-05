
from pathlib import Path
from datetime import datetime
import json


ROOT = Path(
    "/storage/emulated/0/XLevelUp-Deployer"
)


class MetricsCollector:


    def collect(self, result):

        final = result.get(
            "final",
            {}
        )


        files = 0

        try:

            files = len(
                list(
                    ROOT.rglob("*")
                )
            )

        except:

            pass



        return {


            "ENGINE": {

                "status":
                    "ONLINE",

                "name":
                    result.get(
                        "engine",
                        "XDEPLOY"
                    )

            },


            "DEPLOY": {

                "status":
                    final.get(
                        "status",
                        "UNKNOWN"
                    ),

                "mode":
                    final.get(
                        "mode",
                        "TEST"
                    ),

                "time":
                    datetime.now().strftime(
                        "%H:%M:%S"
                    )

            },


            "WORKSPACE": {

                "files":
                    files,

                "status":
                    "READY"

            },


            "GIT": {

                "status":
                    "NOT INITIALIZED",

                "remote":
                    "NONE"

            },


            "AUTH": {

                "status":
                    "MISSING"

            },


            "AI": {

                "status":
                    "READY",

                "memory":
                    "ONLINE"

            },


            "REPAIR": {

                "status":
                    "READY"

            }

        }



metrics = MetricsCollector()
