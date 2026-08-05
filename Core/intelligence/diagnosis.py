import json

from pathlib import Path
from datetime import datetime

from Core.intelligence.rules import RULES



FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/intelligence/data/diagnosis.json"
)



def analyze(
    source,
    error
):

    text = str(error)


    result = None


    for key, rule in RULES.items():

        if key in text:

            result = {

                "time":
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),

                "source":
                    source,

                "problem":
                    rule["type"],

                "cause":
                    rule["cause"],

                "confidence":
                    f'{rule["confidence"]}%',

                "suggestion":
                    rule["suggestion"],

                "raw":
                    text

            }

            break



    if result is None:

        result = {

            "time":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "source":
                source,

            "problem":
                "UNKNOWN_ERROR",

            "cause":
                "No matching rule",

            "confidence":
                "50%",

            "suggestion":
                "Manual inspection required",

            "raw":
                text
        }



    save(result)


    return result




def save(item):

    data = []


    if FILE.exists():

        try:

            data = json.loads(
                FILE.read_text(
                    encoding="utf-8"
                )
            )

        except:

            data = []


    data.append(item)


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




def history():

    if not FILE.exists():

        return []

    return json.loads(
        FILE.read_text(
            encoding="utf-8"
        )
    )
