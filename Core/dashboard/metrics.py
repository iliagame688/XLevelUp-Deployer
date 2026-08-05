from datetime import datetime


def empty():

    return {

        "time":
            datetime.now().strftime(
                "%H:%M:%S"
            ),

        "workspace":
        {
            "path":
            "NOT SET",

            "total":
            0,

            "added":
            0,

            "modified":
            0,

            "deleted":
            0
        },


        "watcher":
        {
            "status":
            "UNKNOWN",

            "events":
            0
        },


        "git":
        {
            "repo":
            "WAITING",

            "branch":
            "-",

            "status":
            "IDLE"
        },


        "recovery":
        {
            "errors":
            0,

            "state":
            "READY"
        }

    }
