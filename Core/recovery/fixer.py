
from Core.dashboard.live.event_bus import bus



class AutoFixer:


    def run(self, diagnosis):


        action = diagnosis["action"]


        if action == "AUTO_MERGE_REQUIRED":

            bus.emit(

                "Trying automatic conflict recovery",

                "AI"

            )


            return True



        return False




fixer = AutoFixer()

