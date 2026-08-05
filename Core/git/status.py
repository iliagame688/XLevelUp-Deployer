from Core.git.gateway import gateway
from Core.git.safe import safe_git
import subprocess



def run_git(path, args):

    try:

        result = subprocess.check_output(

            [
                "git",
                "-C",
                str(path)
            ]
            +
            args,

            stderr=subprocess.STDOUT,

            text=True

        )

        return result.strip()


    except:

        return None




def branch(path):

    result = run_git(
        path,
        [
            "branch",
            "--show-current"
        ]
    )

    return result or "-"




def changes(path):

    result = run_git(
        path,
        [
            "status",
            "--short"
        ]
    )


    if not result:

        return 0


    return len(
        result.splitlines()
    )




def summary(path):

    return {

        "branch":
            branch(path),

        "changes":
            changes(path)

    }
