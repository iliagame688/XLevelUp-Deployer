import json
from pathlib import Path
from datetime import datetime


from Core.engine.hub import engine
from Core.workspace.scanner import scan
from Core.git.manager import inspect
from Core.boot.paths import workspace



RUNTIME = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/runtime.json"
)



def collect():


    ws = workspace()


    data = {

        "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),


        "workspace":
            scan(),


        "git":
            inspect(ws)
            if ws
            else {
                "repo": False
            },


        "services":
            engine.snapshot()

    }


    RUNTIME.write_text(

        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ),

        encoding="utf-8"

    )


    return data




if __name__ == "__main__":

    print(
        collect()
    )
