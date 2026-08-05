
from Core.git.real_engine import real_git
from Core.auth.github_auth import github_auth


class RealDeployOrchestrator:


    def setup(self,path,repo):

        result = {
            "engine":"XLEVELUP_REAL_DEPLOY",
            "steps":[]
        }


        auth = github_auth.setup()


        result["steps"].append({
            "name":"AUTH",
            "status":auth.get("status")
        })


        if auth.get("status") != "READY":

            result["status"]="AUTH_FAILED"
            return result



        real_git.init(
            path
        )


        result["steps"].append({
            "name":"GIT_INIT",
            "status":"READY"
        })


        real_git.remote(
            path,
            repo
        )


        result["steps"].append({
            "name":"REMOTE",
            "status":"CONNECTED"
        })


        upload = real_git.upload(
            path,
            "XLEVELUP AUTO DEPLOY"
        )


        result["steps"].append({
            "name":"UPLOAD",
            "data":upload
        })


        result["status"] = upload.get(
            "status"
        )


        return result



real_orchestrator = RealDeployOrchestrator()
