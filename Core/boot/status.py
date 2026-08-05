
class BootStatus:


    def __init__(self):

        self.steps = []



    def add(
        self,
        name,
        state="OK"
    ):

        self.steps.append({

            "name":
                name,

            "state":
                state

        })



    def summary(self):

        return self.steps



status = BootStatus()
