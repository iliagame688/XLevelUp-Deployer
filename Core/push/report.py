

class PushReport:


    def build(self, result):


        return {


            "operation":

                "PUSH",


            "status":

                result.get(
                    "status"
                ),


            "retry":

                result.get(
                    "retry",
                    0
                )

        }




report = PushReport()

