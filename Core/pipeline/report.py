
class DeployReport:


    def create(self, data):

        return {

            "pipeline":
                "XDEPLOY",

            "status":
                data.get(
                    "status",
                    "UNKNOWN"
                ),

            "steps":
                data.get(
                    "steps",
                    []
                )

        }



report = DeployReport()

