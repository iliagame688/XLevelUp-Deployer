
from Core.github.account import account

from Core.github.status import status

from Core.dashboard.live.event_bus import bus



class GitHubConnector:


    def connect(self, config):


        bus.emit(

            "GitHub connection started",

            "GIT"

        )


        result = account.verify(
            config
        )


        if result:


            bus.emit(

                "GitHub account verified",

                "SUCCESS"

            )


        else:


            bus.emit(

                "GitHub authentication required",

                "ERROR"

            )


        return status.get()




github = GitHubConnector()

