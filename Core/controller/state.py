
class ControllerState:


    def __init__(self):

        self.data = {

            "stage":
                "IDLE",

            "status":
                "WAITING"

        }


    def update(self, stage, status):

        self.data = {

            "stage":
                stage,

            "status":
                status

        }


    def get(self):

        return self.data



state = ControllerState()

