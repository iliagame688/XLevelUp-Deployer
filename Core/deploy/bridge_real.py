from Core.git.real_push import real_push


def run_real():

    result = real_push()

    return {

        "engine":
            "XDEPLOY",

        "mode":
            "REAL",

        "status":
            result.get(
                "status",
                "UNKNOWN"
            ),

        "message":
            result.get(
                "message",
                ""
            ),

        "error":
            result.get(
                "error",
                ""
            )

    }
