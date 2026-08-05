from pathlib import Path
import json
from datetime import datetime


RUNTIME = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/runtime_state.json"
)


class RuntimePanel:

    def __init__(self):
        self.state = {}

    def load(self):

        if RUNTIME.exists():

            try:
                self.state = json.loads(
                    RUNTIME.read_text(
                        encoding="utf-8"
                    )
                )

            except:
                self.state = {}

        return self.state


    def update(self, data):

        self.load()

        self.state.update(data)

        self.state["updated"] = (
            datetime.now()
            .strftime("%Y-%m-%d %H:%M:%S")
        )


        RUNTIME.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        RUNTIME.write_text(
            json.dumps(
                self.state,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )


        return self.state



    def snapshot(self):

        self.load()

        return {

            "ENGINE":
                "ONLINE",

            "DASHBOARD":
                "LIVE",

            "EVENT_BUS":
                "CONNECTED",

            "DEPLOY_MODE":
                self.state.get(
                    "mode",
                    "TEST"
                ),

            "LAST_STATUS":
                self.state.get(
                    "status",
                    "READY"
                ),

            "AI":
                "READY",

            "REPAIR":
                "READY"

        }



runtime_panel = RuntimePanel()
