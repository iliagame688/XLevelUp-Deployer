from Core.deploy.manager import deploy

from Core.dashboard.api import (
    start_dashboard
)



class DeployBridge:


    def launch(self, project):


        dashboard = start_dashboard()


        result = deploy.start(
            project
        )


        return {

            "dashboard":
                dashboard,

            "deploy":
                result

        }




bridge = DeployBridge()
