
from Core.dashboard.live.event_bus import bus


class PushEngine:


    def execute(self, remote):


        bus.emit(

            "Push started",

            "GIT"

        )


        return {


            "remote":

                remote,


            "status":

                "WAITING_AUTH"

        }




push_engine = PushEngine()

