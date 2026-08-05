from Core.dashboard.live.event_bus import bus


class DashboardActions:



    def start_deploy(self, project):


        bus.emit(
            "Deploy started: " + project,
            "RUN"
        )


        return {

            "status":
                "STARTED",

            "project":
                project

        }




    def repair_start(self, error):


        bus.emit(
            "AI Repair: " + error,
            "AI"
        )


        return {

            "status":
                "REPAIRING",

            "error":
                error

        }




actions = DashboardActions()
