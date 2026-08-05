
from Core.deploy.real_orchestrator import real_orchestrator
from Core.config.real_config import GITHUB_REPO



class RealBridge:


    def start(self,path):


        if not GITHUB_REPO:

            return {
                "status":"REPO_MISSING",
                "message":
                "Configure GitHub repository first"
            }


        return real_orchestrator.setup(
            path,
            GITHUB_REPO
        )



real_bridge = RealBridge()
