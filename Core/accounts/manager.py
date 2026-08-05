from Core.accounts.models import GitAccount


class AccountManager:



    def __init__(self):

        self.accounts = []



    def add_account(
        self,
        name
    ):


        account = GitAccount(
            name
        )


        self.accounts.append(
            account
        )


        return account



    def list(self):

        return [

            item.status()

            for item in self.accounts

        ]




accounts = AccountManager()
