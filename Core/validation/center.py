from Core.validation.scanner import scanner

from Core.validation.health import health

from Core.dashboard.live.event_bus import bus



class SelfTestCenter:



    def run(self):


        modules = [


            "Core.strategy.engine",

            "Core.git_engine.manager",

            "Core.accounts.manager",

            "Core.dashboard.api"

        ]



        bus.emit(

            "System self test started",

            "TEST"

        )


        results = scanner.scan(
            modules
        )


        report = health.analyze(
            results
        )


        bus.emit(

            "Self test completed",

            report["status"]

        )


        return {


            "report":
                report,


            "details":
                results

        }




self_test = SelfTestCenter()
