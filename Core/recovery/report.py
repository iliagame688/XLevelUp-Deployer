
class RecoveryReport:


    def create(self, diagnosis):

        return {

            "error_type":
                diagnosis["type"],

            "next_action":
                diagnosis["action"]

        }




report = RecoveryReport()

