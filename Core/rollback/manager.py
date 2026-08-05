

import os
import shutil


def rollback(snapshot):


    if os.path.exists(snapshot):

        shutil.copytree(
        snapshot,
        ".",
        dirs_exist_ok=True
        )


        return True


    return False


