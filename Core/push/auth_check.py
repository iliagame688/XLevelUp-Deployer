
class AuthChecker:


    def check(self, config):


        if not config:

            return {

                "ready":
                    False,

                "reason":
                    "AUTH_REQUIRED"

            }


        if config.get("auth"):

            return {

                "ready":
                    True,

                "method":
                    config["auth"]

            }


        return {

            "ready":
                False,

            "reason":
                "AUTH_REQUIRED"

        }




checker = AuthChecker()

