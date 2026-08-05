
from pathlib import Path
import time


from Core.dashboard.live.event_bus import bus



class UploadEngine:


    def scan(self, workspace):


        files = []


        root = Path(
            workspace
        )


        for item in root.rglob("*"):


            if item.is_file():

                files.append(item)



        return files




    def upload(self, workspace):


        files = self.scan(
            workspace
        )


        total = len(
            files
        )


        uploaded = 0



        bus.emit(

            "Upload started",

            "UPLOAD",

            0

        )



        for file in files:


            uploaded += 1


            percent = int(

                uploaded

                /

                max(total,1)

                *

                100

            )


            bus.emit(

                f"Uploading {file.name[:20]}",

                "UPLOAD",

                percent

            )


            time.sleep(
                0.02
            )



        bus.emit(

            "Upload finished",

            "SUCCESS",

            100

        )



        return {


            "files":

                total,


            "status":

                "SUCCESS"


        }





upload = UploadEngine()

