from Core.git_engine.changes import changes

from Core.git_engine.planner import planner

from Core.dashboard.live.event_bus import bus



class GitIntelligence:


    def analyze(self, path):


        bus.emit(
            "Detecting workspace changes",
            "GIT"
        )


        diff = changes.compare(
            path
        )


        plan = planner.create(
            diff
        )


        bus.emit(
            f"Deploy plan: {plan['action']}",
            "READY"
        )


        return {


            "changes":
                diff,


            "plan":
                plan

        }




intelligence = GitIntelligence()
