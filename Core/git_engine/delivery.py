from Core.git_engine.auth import auth

from Core.git_engine.push import push



class DeliveryPipeline:


    def run(self, commit):


        auth_state = auth.check()


        if not auth_state["authenticated"]:


            return {


                "status":
                    "WAITING_AUTH",


                "message":
                    "Git authentication required"

            }



        prepared = push.prepare(
            commit
        )


        return push.execute(
            prepared
        )





delivery = DeliveryPipeline()
