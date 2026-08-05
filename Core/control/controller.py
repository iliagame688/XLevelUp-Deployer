from Core.control.state import state

from Core.control.events import events

from Core.control.tabs import tabs



class XControl:


    def __init__(self):

        self.name = (
            "XCONTROL CENTER"
        )



    def boot(self):

        events.emit(
            "CONTROL_BOOT",
            {
                "status":
                    "ONLINE"
            }
        )


        state.update(
            "status",
            "RUNNING"
        )


        return self.snapshot()



    def switch_tab(
        self,
        tab
    ):

        result = tabs.open(
            tab
        )


        if result["status"] == "ACTIVE":

            state.update(
                "active_tab",
                tab
            )


            events.emit(
                "TAB_CHANGED",
                {
                    "tab":
                        tab
                }
            )


        return result




    def snapshot(self):

        return {

            "state":
                state.snapshot(),

            "tabs":
                tabs.list(),

            "events":
                events.history()

        }





control = XControl()
