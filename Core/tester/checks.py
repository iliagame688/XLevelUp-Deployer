
from pathlib import Path


class SystemChecks:


    def workspace(self, path):

        return Path(path).exists()



    def module(self, name):

        try:

            __import__(name)

            return True


        except Exception:

            return False



    def run_all(self, path):


        return {

            "WORKSPACE":

                self.workspace(path),


            "DASHBOARD":

                self.module(
                    "Core.dashboard.app"
                ),


            "UPLOAD":

                self.module(
                    "Core.upload.engine"
                ),


            "PIPELINE":

                self.module(
                    "Core.pipeline.deploy"
                ),


            "RECOVERY":

                self.module(
                    "Core.recovery.analyzer"
                )

        }





checks = SystemChecks()

