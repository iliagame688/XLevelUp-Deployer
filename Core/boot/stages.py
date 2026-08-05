from Core.boot.status import status


class BootStages:



    def run(self):


        stages = [

            "CORE CHECK",

            "SELF TEST",

            "CLEANUP SCAN",

            "OPTIMIZER SCAN",

            "DASHBOARD LOAD"

        ]


        for stage in stages:

            status.add(
                stage
            )


        return status.summary()




stages = BootStages()
