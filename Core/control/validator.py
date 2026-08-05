import re



class Validator:


    def token(self, value):

        result = {

            "valid":
                False,

            "status":
                "INVALID",

            "reason":
                ""

        }


        if not value:

            result["reason"] = "Empty token"

            return result



        patterns = [

            r"^ghp_[A-Za-z0-9]+$",

            r"^github_pat_[A-Za-z0-9_]+$"

        ]


        if any(
            re.match(
                p,
                value
            )
            for p in patterns
        ):

            result["valid"] = True

            result["status"] = "VALID"

            result["reason"] = "Token format accepted"


        else:

            result["reason"] = "Invalid token format"


        return result




validator = Validator()
