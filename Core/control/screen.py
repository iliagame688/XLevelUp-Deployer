import os
import platform



def clear():

    os.system(
        "clear"
    )



def device():

    return {

        "platform":
            platform.system(),

        "python":
            platform.python_version()

    }
