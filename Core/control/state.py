class StateManager:


    def __init__(self):

        self.state = {

            "engine":
                "ONLINE",

            "active_tab":
                "HOME",

            "status":
                "READY"

        }



    def update(
        self,
        key,
        value
    ):

        self.state[key] = value



    def snapshot(self):

        return self.state.copy()



state = StateManager()
