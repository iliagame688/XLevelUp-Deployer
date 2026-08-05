from pathlib import Path
import json
import uuid
from datetime import datetime


BASE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data"
)


RUNTIME = BASE / "intelligence.json"


class DashboardIntelligence:


    def __init__(self):
        self.data = {}


    def collect(self, deploy_result=None):

        self.data = {

            "session":
                str(uuid.uuid4())[:8],

            "time":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "engine":
                "ONLINE",

            "mode":
                "TEST",

            "git":
                "NOT INITIALIZED",

            "auth":
                "MISSING",

            "modules":
                {
                    "ENGINE":
                        "READY",

                    "DEPLOY":
                        "READY",

                    "AI":
                        "READY",

                    "REPAIR":
                        "READY"
                },

            "deploy":
                {

                    "status":
                        (
                            deploy_result
                            .get("final", {})
                            .get(
                                "status",
                                "UNKNOWN"
                            )
                            if deploy_result
                            else
                            "UNKNOWN"
                        ),

                    "steps":
                        len(
                            deploy_result.get(
                                "steps",
                                []
                            )
                        )
                        if deploy_result
                        else
                        0
                }

        }


        self.save()

        return self.data



    def save(self):

        BASE.mkdir(
            parents=True,
            exist_ok=True
        )


        RUNTIME.write_text(
            json.dumps(
                self.data,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )


    def snapshot(self):

        if RUNTIME.exists():

            try:

                return json.loads(
                    RUNTIME.read_text(
                        encoding="utf-8"
                    )
                )

            except:

                pass


        return {}



intelligence = DashboardIntelligence()
