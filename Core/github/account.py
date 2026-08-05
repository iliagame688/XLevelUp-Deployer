
from Core.github.status import status



class AccountManager:


    def verify(self, config):


        auth = config.get(
            "auth"
        )


        account = config.get(
            "account"
        )


        if not auth:

            return False


        status.update({

            "connected":
                True,

            "account":
                account,

            "auth":
                auth

        })


        return True




account = AccountManager()

