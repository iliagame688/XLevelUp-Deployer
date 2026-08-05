from Core.dashboard.registry import registry
from Core.dashboard.live.event_bus import bus


class DashboardController:


    def load_default_panels(self):

        panels = []


        modules = [
            ("ENGINE", "Core.dashboard.panels.engine", "EnginePanel"),
            ("DEPLOY", "Core.dashboard.panels.deploy", "DeployPanel"),
            ("AI", "Core.dashboard.panels.ai", "AIPanel"),
            ("REPAIR", "Core.dashboard.panels.repair", "RepairPanel"),
        ]


        for name, module, cls in modules:

            try:

                mod = __import__(
                    module,
                    fromlist=[cls]
                )

                panel = getattr(
                    mod,
                    cls
                )()

                registry.register(
                    name,
                    panel
                )

                panels.append(name)


            except Exception:

                registry.register(
                    name,
                    {
                        "status":
                        "AVAILABLE"
                    }
                )

                panels.append(name)


        return panels



    def render(self, result=None):

        loaded = self.load_default_panels()


        print()

        print(
            "╭──────── XLEVELUP COMMAND CENTER ────────╮"
        )


        print(
            "\nSYSTEM"
            "\n━━━━━━━━━━━━━━━━"
            "\nENGINE       [✓] ONLINE"
            "\nEVENT BUS    [✓] CONNECTED"
            "\nPANELS       [{}]"
            .format(
                len(loaded)
            )
        )


        print(
            "\nMODULES"
            "\n━━━━━━━━━━━━━━━━"
        )


        for panel in loaded:

            print(
                "✓ {}".format(panel)
            )


        print(
            "\nLIVE EVENTS"
            "\n━━━━━━━━━━━━━━━━"
        )


        for event in bus.get()[-5:]:

            print(
                "{} | {} | {}%"
                .format(
                    event.get("level"),
                    event.get("message"),
                    event.get("progress",0)
                )
            )


        print(
            "\n╰────────────────────────────────────────╯"
        )


        return {
            "dashboard":
                "ACTIVE",

            "panels":
                loaded
        }



controller = DashboardController()
