
from pathlib import Path
import json

FLAG = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/real_mode.json"
)


def enable_real():

    FLAG.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    FLAG.write_text(
        json.dumps(
            {
                "enabled": True
            },
            indent=4
        ),
        encoding="utf-8"
    )

    print("✓ REAL DEPLOY ENABLED")


def is_real():

    if not FLAG.exists():
        return False

    try:
        return json.loads(
            FLAG.read_text()
        ).get(
            "enabled",
            False
        )

    except:
        return False
