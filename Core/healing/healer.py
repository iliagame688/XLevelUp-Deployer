from Core.intelligence.analyzer import analyzer

from Core.healing.verifier import verify

from Core.healing.history import save



class SelfHealer:


    MAX_RETRY = 3



    def repair(self,error):


        analysis = analyzer.analyze(
            error
        )


        result = {


            "error":
                error,

            "type":
                analysis["type"],

            "mode":
                analysis["mode"],

            "action":
                analysis["action"]

        }



        if analysis["mode"] == "AUTO":


            result["attempts"] = 1


            check = verify(
                analysis["action"]
            )


            result.update(
                check
            )


        else:


            result["status"] = (
                "WAITING_USER"
            )



        save(result)


        return result




healer = SelfHealer()

