from datetime import datetime


def summary(
    module,
    checks,
    status
):

    return {

        "module":
            module,

        "status":
            status,

        "checks":
            checks,

        "time":
            datetime.now().strftime(
                "%H:%M:%S"
            )

    }
