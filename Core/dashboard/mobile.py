import shutil


def terminal_width():

    try:
        return shutil.get_terminal_size().columns

    except:
        return 60



def is_mobile():

    return terminal_width() < 90
