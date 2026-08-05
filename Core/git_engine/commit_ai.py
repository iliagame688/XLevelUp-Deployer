from Core.git_engine.summary import summary


class CommitIntelligence:


    def generate(self, changes):


        data = summary.build(
            changes
        )


        if data["added"]:

            commit_type = "feature"


        elif data["removed"]:

            commit_type = "cleanup"


        else:

            commit_type = "update"



        message = (

            f"{commit_type}: "

            f"{data['modified']} files updated"

        )


        return {


            "type":
                commit_type,


            "message":
                message,


            "summary":
                data

        }




commit_ai = CommitIntelligence()
