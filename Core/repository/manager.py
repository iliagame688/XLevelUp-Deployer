
from Core.repository.status import status

from Core.repository.remote import remote

from Core.dashboard.live.event_bus import bus



class RepositoryManager:


    def setup(self, mode, name):


        bus.emit(

            "Repository setup started",

            "GIT"

        )


        if mode == "CREATE":

            bus.emit(

                "New repository prepared",

                "SUCCESS"

            )


        else:

            bus.emit(

                "Existing repository selected",

                "SUCCESS"

            )


        result = remote.configure(
            name
        )


        status.update({

            "repo":
                name,

            "mode":
                mode

        })


        return status.get()




repository = RepositoryManager()

