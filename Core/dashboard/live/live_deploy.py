
from Core.dashboard.live.progress import progress



class LiveDeploy:


    def start(self):


        print("""
╭──────────────────────────╮
│ XDEPLOY LIVE OPERATIONS  │
╰──────────────────────────╯
""")


        stages = [

            "WORKSPACE CHECK",

            "FILE UPLOAD",

            "COMMIT",

            "REMOTE PUSH"

        ]


        for stage in stages:

            progress.run(
                stage
            )



        print(
"""
╭──────────────────────────╮
│ DEPLOY COMPLETE ✓        │
╰──────────────────────────╯
"""
        )



live = LiveDeploy()

