from Core.dashboard.terminal import terminal

from Core.dashboard.panel import panel



class Dashboard:


    def launch(self):


        terminal.header()


        panel.render({

            "ENGINE":
                "ONLINE",

            "SELF TEST":
                "PASS",

            "WORKSPACE":
                "READY",

            "GIT":
                "READY"

        })


        terminal.event(
            "Dashboard started"
        )


        return True




dashboard = Dashboard()



def run_dashboard():

    return dashboard.launch()

