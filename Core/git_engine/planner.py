from datetime import datetime



class DeployPlanner:


    def create(self, changes):


        total = (

            len(changes["added"])

            +

            len(changes["modified"])

            +

            len(changes["removed"])

        )


        return {


            "created":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),


            "files":
                total,


            "action":

                "DEPLOY"

                if total

                else

                "NO_CHANGES"

        }




planner = DeployPlanner()
