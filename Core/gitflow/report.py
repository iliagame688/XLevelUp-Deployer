

class CommitReport:


    def build(self, result):


        return {


            "operation":

                "COMMIT",


            "status":

                result.get(
                    "status"
                ),


            "files":

                result.get(
                    "changes",
                    0
                ),


            "message":

                result.get(
                    "message"
                )

        }




report = CommitReport()

