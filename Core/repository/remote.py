
from Core.repository.status import status



class RemoteManager:


    def configure(self, name):


        remote = {

            "repo":
                name,

            "url":
                f"github.com/{name}"

        }


        status.update({

            "remote":
                remote["url"]

        })


        return remote




remote = RemoteManager()

