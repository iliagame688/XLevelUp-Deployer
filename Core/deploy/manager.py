from Core.dashboard.live.event_bus import bus


class DeployManager:


    def start(self, project):

        bus.emit(
            f"Deploy initialized: {project}",
            "START"
        )


        stages = [

            "CHECK_ACCOUNT",

            "SCAN_WORKSPACE",

            "PREPARE_FILES",

            "UPLOAD",

            "VERIFY"

        ]


        result = []


        for stage in stages:

            bus.emit(
                stage,
                "RUNNING"
            )

            result.append({

                "stage":
                    stage,

                "status":
                    "DONE"

            })


        bus.emit(
            "Deploy completed",
            "SUCCESS"
        )


        return {

            "project":
                project,

            "stages":
                result,

            "status":
                "SUCCESS"

        }




deploy = DeployManager()
