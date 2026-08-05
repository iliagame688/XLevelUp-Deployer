
class RepositoryWizard:


    def select(self):

        print("""
╭──────────────────────╮
│ REPOSITORY           │
╰──────────────────────╯

[1] Create Repository
[2] Existing Repository
        """)


        choice=input(
            "Choice: "
        )


        return {

            "1":
            "CREATE",

            "2":
            "EXISTING"

        }.get(
            choice,
            "CREATE"
        )




repository = RepositoryWizard()

