from pathlib import Path
import json



class StatusHub:


    def project(self):

        path = Path(
            "/storage/emulated/0/XLevelUp-Deployer"
        )


        files = 0


        if path.exists():

            for _ in path.rglob("*"):

                files += 1


        return {

            "files":
                files,

            "status":
                "CONNECTED"

        }



    def github(self):

        file = Path(
            "/storage/emulated/0/XLevelUp-Deployer/Core/data/github_status.json"
        )


        if not file.exists():

            return {

                "status":
                    "WAITING",

                "account":
                    "-"

            }


        try:

            data = json.loads(
                file.read_text(
                    encoding="utf-8"
                )
            )


            return {

                "status":
                    data.get(
                        "status",
                        "UNKNOWN"
                    ),

                "account":
                    data.get(
                        "user",
                        "-"
                    )

            }


        except:

            return {

                "status":
                    "ERROR",

                "account":
                    "-"

            }




    def snapshot(self):

        return {

            "CORE":
                "🟢 ONLINE",

            "PROJECT":
                self.project(),

            "GITHUB":
                self.github(),

            "INTELLIGENCE":
                "🟢 ACTIVE"

        }



status = StatusHub()
