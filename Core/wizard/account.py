
class AccountWizard:


    def select(self):


        print("""
╭──────────────────────╮
│ ACCOUNT              │
╰──────────────────────╯

[1] Existing Account
[2] Add Account
        """)


        choice=input(
            "Choice: "
        )


        return {

            "1":
            "EXISTING",

            "2":
            "NEW"

        }.get(
            choice,
            "NEW"
        )




account = AccountWizard()

