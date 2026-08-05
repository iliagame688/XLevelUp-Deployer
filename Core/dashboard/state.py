
class DashboardState:


    def __init__(self):

        self.status = "OFFLINE"

        self.mode = "IDLE"



    def online(self):

        self.status = "ONLINE"



    def set_mode(self, mode):

        self.mode = mode



    def snapshot(self):

        return {

            "status":
                self.status,

            "mode":
                self.mode

        }




state = DashboardState()

