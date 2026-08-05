from Core.intelligence.classifier import classify

from Core.intelligence.repair import repair



class ErrorAnalyzer:


    def analyze(
        self,
        error
    ):


        error_type = classify(
            error
        )


        result = {

            "error":
                str(error),

            "type":
                error_type

        }


        if error_type.startswith(
            "AUTO"
        ):

            result["mode"] = "AUTO"

            result["action"] = repair(
                error_type
            )


        elif error_type.startswith(
            "USER"
        ):

            result["mode"] = "USER"

            result["action"] = (
                "User intervention required"
            )


        else:

            result["mode"] = "UNKNOWN"

            result["action"] = (
                "Analyze manually"
            )


        return result




analyzer = ErrorAnalyzer()



def analyze(error):

    return analyzer.analyze(
        error
    )
