
from Core.wizard.auth import auth

from Core.wizard.account import account

from Core.wizard.repository import repository



class DeployWizard:


    def run(self):


        print(
"\nXDEPLOY DEPLOY WIZARD\n"
        )


        config={}


        config["auth"] = (
            auth.select()
        )


        config["account"] = (
            account.select()
        )


        config["repository"] = (
            repository.select()
        )


        print(
            "\nCONFIG READY:"
        )


        print(config)


        return config




wizard = DeployWizard()

