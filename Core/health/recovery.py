def analyze(error):

    text = str(error).lower()


    if "permission" in text:

        return {
            "type": "PERMISSION",
            "solution":
                "Check account access"
        }


    if "auth" in text or "token" in text:

        return {
            "type": "AUTH",
            "solution":
                "Update access token"
        }


    if "network" in text or "connection" in text:

        return {
            "type": "NETWORK",
            "solution":
                "Check internet connection"
        }


    return {

        "type":
            "UNKNOWN",

        "solution":
            "Inspect deployment logs"

    }
