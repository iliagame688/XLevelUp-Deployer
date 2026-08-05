from datetime import datetime



def stage(name, status, detail=""):

    return {

        "stage":
            name,

        "status":
            status,

        "detail":
            detail,

        "time":
            datetime.now().strftime(
                "%H:%M:%S"
            )

    }
