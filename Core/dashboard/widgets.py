def status_icon(status):

    icons = {

        "ONLINE": "🟢",

        "READY": "🟢",

        "RUNNING": "🟡",

        "FAILED": "🔴",

        "OFFLINE": "⚫"

    }


    return icons.get(
        status,
        "⚪"
    )
