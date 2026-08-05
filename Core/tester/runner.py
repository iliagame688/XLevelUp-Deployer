
from Core.tester.checks import checks

from Core.tester.report import report

from Core.dashboard.live.event_bus import bus



class TestRunner:


    def execute(self, workspace):


        bus.emit(

            "System test started",

            "TEST"

        )


        result = checks.run_all(

            workspace

        )


        final = report.build(

            result

        )


        if final["ready"]:


            bus.emit(

                "All tests passed",

                "SUCCESS"

            )


        else:


            bus.emit(

                "System check failed",

                "ERROR"

            )


        return final




tester = TestRunner()

