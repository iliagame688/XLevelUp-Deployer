from pathlib import Path


def find_repo(path):

    current = Path(path).resolve()


    while current != current.parent:

        if (current / ".git").exists():
            return current

        current = current.parent


    return None
