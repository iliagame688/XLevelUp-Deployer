
from getpass import getpass



class AuthManager:


    def select(self):


        print("""
╭──────── AUTH ────────╮

[1] GitHub Token
[2] SSH Key

╰──────────────────────╯
""")


        choice = input(
            "Choice: "
        )


        if choice == "1":


            token = getpass(
                "GitHub Token: "
            )


            return {

                "type":
                    "TOKEN",

                "token":
                    token

            }



        elif choice == "2":


            key = input(
                "SSH Key Path: "
            )


            return {

                "type":
                    "SSH",

                "key":
                    key

            }



        else:


            return None




auth = AuthManager()

