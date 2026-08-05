

from getpass import getpass


from Core.vault.auth import vault



def setup_auth():


    print("""

╭──────── AUTH SETUP ────────╮

[1] GitHub Token
[2] SSH Key

╰────────────────────────────╯

""")


    method = input(

        "Choice: "

    )



    if method == "1":


        token = getpass(

            "Token: "

        )


        data = {

            "type":

                "TOKEN",

            "token":

                token

        }



    else:


        key = input(

            "SSH Path: "

        )


        data = {

            "type":

                "SSH",

            "key":

                key

        }



    vault.save(

        data

    )


    print(

        "\n✓ AUTH SAVED"

    )


    return data




