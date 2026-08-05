from Core.dashboard.live.event_bus import bus


class PushManager:


    def prepare(self, commit):


        bus.emit(
            "Preparing push request",
            "GIT"
        )


        return {


            "commit":
                commit,


            "ready":
                True

        }




    def execute(self, data):


        bus.emit(
            "Push started",
            "RUNNING"
        )


        # اینجا بعداً Git subprocess واقعی وصل می‌شود


        bus.emit(
            "Push completed",
            "SUCCESS"
        )


        return {


            "status":
                "SUCCESS",


            "details":
                data

        }





push = PushManager()
