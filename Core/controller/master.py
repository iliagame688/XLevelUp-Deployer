
from Core.tester.runner import tester

from Core.dashboard.controller import controller

from Core.controller.state import state

from Core.dashboard.live.event_bus import bus



class MasterController:



    def start(self, workspace, config):


        print(

"""
╭──────────────────────────╮
│ XLEVELUP MASTER CORE     │
╰──────────────────────────╯
"""

        )


        # TEST

        state.update(
            "SYSTEM TEST",
            "RUNNING"
        )


        test = tester.execute(
            workspace
        )


        if not test["ready"]:


            state.update(
                "SYSTEM TEST",
                "FAILED"
            )


            return {

                "status":
                    "BLOCKED",

                "reason":
                    "TEST_FAILED"

            }


        state.update(
            "SYSTEM TEST",
            "PASSED"
        )



        # READY

        bus.emit(

            "System ready for deploy",

            "SUCCESS"

        )


        state.update(

            "DEPLOY",

            "READY"

        )


        result = {


            "status":

                "READY",


            "controller":

                "MASTER v3.0",


            "test":

                test

        }



        controller.show_result(

            result

        )


        return result




master = MasterController()

