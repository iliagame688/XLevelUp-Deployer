import json

from pathlib import Path


FILE = Path(
"/storage/emulated/0/XLevelUp-Deployer/Core/data/integrity_report.json"
)



def save(data):

    FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    FILE.write_text(

        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ),

        encoding="utf-8"

    )
