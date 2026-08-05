import shutil


def detect():

    width = shutil.get_terminal_size().columns


    if width < 60:

        return "COMPACT"


    elif width < 100:

        return "MOBILE"


    return "FULL"

