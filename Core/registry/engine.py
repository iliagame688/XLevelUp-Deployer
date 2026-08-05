import json

from pathlib import Path


FILE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/registry.json"
)



class EngineRegistry:


    def __init__(self):

        self.engines = {}



    def register(
        self,
        name,
        status="READY"
    ):

        self.engines[name] = {

            "status":
                status

        }


        self.save()


        return self.engines[name]




    def update(
        self,
        name,
        status
    ):

        if name in self.engines:

            self.engines[name]["status"] = status

            self.save()




    def save(self):

        FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        FILE.write_text(

            json.dumps(
                self.engines,
                indent=4,
                ensure_ascii=False
            ),

            encoding="utf-8"

        )




    def snapshot(self):

        return self.engines.copy()



engine_registry = EngineRegistry()
