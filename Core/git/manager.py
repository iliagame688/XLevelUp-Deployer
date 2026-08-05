from Core.git.detector import find_repo
from Core.git.status import summary



def inspect(path):

    repo = find_repo(path)


    if not repo:

        return {

            "repo":
                False,

            "status":
                "NOT A REPO"

        }



    data = summary(repo)


    return {

        "repo":
            True,

        "path":
            str(repo),

        "branch":
            data["branch"],

        "changes":
            data["changes"]

    }
