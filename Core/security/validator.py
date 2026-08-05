from Core.security.credentials import load



class CredentialValidator:



    def check(

        self,

        account

    ):


        items = load()


        for item in items:


            if item["account"] == account:


                value = item["credential_id"]


                if value:

                    item["status"] = "VALID"

                    return {

                        "status":
                            "VALID",

                        "account":
                            account,

                        "icon":
                            "🟢"

                    }



                item["status"] = "INVALID"


                return {

                    "status":
                        "INVALID",

                    "icon":
                        "🔴"

                }




        return {

            "status":
                "NOT_FOUND",

            "icon":
                "⚪"

        }





validator = CredentialValidator()
