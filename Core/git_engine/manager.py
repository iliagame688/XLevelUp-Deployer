
from Core.git_engine.scanner import scanner

from Core.git_engine.analyzer import analyzer

from Core.dashboard.live.event_bus import bus



class GitManager:


    def inspect(self, path):


        bus.emit(
            "Git scan started",
            "GIT"
        )


        repo = scanner.scan(
            path
        )


        analysis = analyzer.analyze(
            path
        )


        bus.emit(
            "Git analysis completed",
            "SUCCESS"
        )


        return {


            "repository":
                repo,


            "analysis":
                analysis

        }




git = GitManager()
