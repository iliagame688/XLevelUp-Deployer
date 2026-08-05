from pathlib import Path


ROOT = Path(
    "/storage/emulated/0/XLevelUp-Deployer"
)


CORE = ROOT / "Core"

CONFIG = CORE / "config"

DATA = CORE / "data"

LOGS = CORE / "logs"


def workspace():

    config = CONFIG / "settings.json"


    if config.exists():

        import json

        try:

            data = json.loads(
                config.read_text(
                    encoding="utf-8"
                )
            )

            return Path(
                data.get(
                    "workspace",
                    ""
                )
            )

        except:

            pass


    return None



def info():

    return {

        "root":
            str(ROOT),

        "core":
            str(CORE),

        "config":
            str(CONFIG),

        "data":
            str(DATA),

        "logs":
            str(LOGS),

        "workspace":
            str(workspace())
            if workspace()
            else "NOT SET"

    }
