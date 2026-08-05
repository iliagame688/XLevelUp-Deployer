from pathlib import Path
from Core.auth.github_auth import github_auth
from Core.git.real_push import real_push


class RealDeploy:

    def run(self, path):

        auth = github_auth.setup()

        if auth.get("status") != "READY":
            return {
                "status": "AUTH_REQUIRED"
            }

        git = real_push.run(path)

        return {
            "status": "UNKNOWN",
            "auth": auth,
            "git": git
        }


real_deploy = RealDeploy()
