from pathlib import Path


def find_repo(path):

    current = Path(path)


    if not current.exists():

        return None



    for folder in [current] + list(current.parents):

        if (folder / ".git").exists():

            return folder



    return None
