
import subprocess
import time

from Core.dashboard.live.event_bus import bus



class PushEngine:


    def git(self, args):

        try:

            result = subprocess.check_output(

                ["git"] + args,

                stderr=subprocess.STDOUT

            )


            return {

                "ok":

                    True,

                "output":

                    result.decode(

                        errors="ignore"

                    )

            }


        except Exception as e:


            return {

                "ok":

                    False,

                "output":

                    str(e)

            }



    def check_remote(self):


        bus.emit(

            "Checking remote repository",

            "PUSH",

            10

        )


        result = self.git(

            [

                "remote",

                "-v"

            ]

        )


        return result




    def run(self, remote="origin", *args, **kwargs):


        self.check_remote()



        bus.emit(

            "Preparing push",

            "PUSH",

            30

        )



        for retry in range(3):


            result = self.git(

                [

                    "push",

                    remote

                ]

            )


            if result["ok"]:


                bus.emit(

                    "Push completed",

                    "SUCCESS",

                    100

                )


                return {


                    "status":

                        "SUCCESS",


                    "retry":

                        retry,


                    "output":

                        result["output"]

                }



            bus.emit(

                f"Push retry {retry+1}",

                "WARNING",

                50 + retry * 10

            )


            time.sleep(
                1
            )



        bus.emit(

            "Push failed",

            "ERROR",

            100

        )


        return {


            "status":

                "FAILED",


            "output":

                result["output"]

        }




push = PushEngine()

