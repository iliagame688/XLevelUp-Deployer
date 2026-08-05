from Core.dashboard.live.event_bus import bus
from Core.dashboard.registry import registry


from Core.dashboard.runtime_panel import runtime_panel
from Core.dashboard.collector import metrics


class DashboardKernel:


    def __init__(self):

        self.status = {
            "engine": "OFFLINE",
            "panels": [],
            "events": []
        }



    def boot(self):

        self.load_panels()

        bus.emit(
            "DASHBOARD KERNEL ONLINE",
            "SUCCESS",
            100
        )


        self.status["engine"] = "ONLINE"


    def load_panels(self):

        panels = [
            "ENGINE",
            "DEPLOY",
            "AUTH",
            "GIT",
            "AI",
            "REPAIR"
        ]


        for p in panels:

            registry.register(
                p,
                {
                    "status":
                    "READY"
                }
            )


        self.status["panels"] = panels



    def snapshot(self):

        self.status["events"] = bus.get()

        
        self.status["runtime"] = metrics.collect(
            self.status
        )

        return self.status




kernel = DashboardKernel()
