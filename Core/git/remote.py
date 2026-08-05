from Core.git.gateway import gateway
from Core.git.safe import safe_git
import subprocess



def get_remote(repo):

    try:

        result = subprocess.run(
            [
                "git",
                "-C",
                str(repo),
                "remote",
                "-v"
            ],
            capture_output=True,
            text=True
        )


        return result.stdout.strip()


    except Exception:

        return ""
