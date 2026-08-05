
import subprocess
import time

from Core.dashboard.live.event_bus import bus



class CommitEngine:


    def git(self, args):

        try:

            result = subprocess.check_output(

                ["git"] + args,

                stderr=subprocess.STDOUT

            )


            return result.decode(
                errors="ignore"
            )


        except Exception as e:

            return str(e)



    def status(self):


        result = self.git(

            [

                "status",

                "--short"

            ]

        )


        return [

            x for x in result.splitlines()

            if x.strip()

        ]




    def create(self, message=None):


        bus.emit(

            "Checking git changes",

            "GIT",

            10

        )


        changes = self.status()



        if not changes:


            bus.emit(

                "No changes detected",

                "GIT",

                100

            )


            return {


                "status":

                    "EMPTY",


                "changes":

                    0

            }



        bus.emit(

            f"{len(changes)} files changed",

            "GIT",

            30

        )



        self.git(

            [

                "add",

                "."

            ]

        )



        bus.emit(

            "Files staged",

            "GIT",

            60

        )



        if not message:


            message = (

                "XDEPLOY automated update"

            )



        commit_result = self.git(

            [

                "commit",

                "-m",

                message

            ]

        )



        time.sleep(
            0.1
        )



        bus.emit(

            "Commit created",

            "SUCCESS",

            100

        )



        return {


            "status":

                "SUCCESS",


            "message":

                message,


            "changes":

                len(changes),


            "output":

                commit_result

        }




commit_engine = CommitEngine()

