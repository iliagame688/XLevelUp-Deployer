
class ErrorAnalyzer:


    def analyze(self, error):


        msg = error.lower()


        if "token" in msg:

            return {

                "type":
                    "AUTH",

                "action":
                    "USER_TOKEN_REQUIRED"

            }


        if "permission" in msg:

            return {

                "type":
                    "PERMISSION",

                "action":
                    "CHECK_ACCESS"

            }


        if "conflict" in msg:

            return {

                "type":
                    "GIT_CONFLICT",

                "action":
                    "AUTO_MERGE_REQUIRED"

            }


        return {

            "type":
                "UNKNOWN",

            "action":
                "MANUAL_CHECK"

        }




analyzer = ErrorAnalyzer()

