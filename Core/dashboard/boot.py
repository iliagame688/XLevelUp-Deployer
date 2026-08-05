
from Core.dashboard.kernel import kernel
from Core.dashboard.intelligence import intelligence


class DashboardBoot:


    def __init__(self):

        self.ready = False



    def start(self, result):


        try:

            intelligence.collect(
                result
            )

            state = kernel.snapshot()


            runtime = state.get(
                "runtime",
                {}
            )


            print()

            print(
                "╭──────── XLEVELUP RUNTIME CENTER ────────╮"
            )


            if runtime:

                for name,data in runtime.items():

                    if isinstance(data, dict):

                        status = data.get(
                            "status",
                            "-"
                        )

                        print(
                            f"{name:<12} | {status}"
                        )

                    else:

                        print(
                            f"{name:<12} | {data}"
                        )

            else:

                print(
                    "SYSTEM       | ONLINE"
                )


            print(
                "╰──────────────────────────────────────────╯"
            )


            self.ready = True


        except Exception as e:

            print(
                "Dashboard Boot Error:",
                e
            )


        return self.ready



boot = DashboardBoot()
