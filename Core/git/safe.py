
from pathlib import Path


def safe_git(path="."):

    if not Path(path, ".git").exists():

        return {

            "allowed": False,

            "mode": "TEST",

            "message":
            "Git disabled - repository missing"

        }


    return {

        "allowed": True,

        "mode": "REAL",

        "message":
        "Git available"

    }

