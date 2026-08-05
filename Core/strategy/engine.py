
from Core.strategy.rules import DEPLOY_RULES

from Core.dashboard.live.event_bus import bus



class StrategyEngine:



    def select(self, project):


        project_type = project.get(

            "type",

            "UNKNOWN"

        )


        strategy = DEPLOY_RULES.get(

            project_type,

            DEPLOY_RULES["UNKNOWN"]

        )


        bus.emit(

            f"Strategy selected: {strategy['flow']}",

            "AI"

        )


        return {


            "project_type":
                project_type,


            "strategy":
                strategy

        }




strategy = StrategyEngine()

