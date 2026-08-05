from Core.deploy.detector import detector
from Core.deploy.profile import create



class DeployAdapter:



    def analyze(self, path):


        detected = detector.detect(
            path
        )


        profile = {

            "workspace":
                path,

            "platform":
                detected["platform"],

            "auto_deploy":
                True,

            "health_check":
                True,

            "status":
                "READY"

        }


        return create(profile)



adapter = DeployAdapter()
