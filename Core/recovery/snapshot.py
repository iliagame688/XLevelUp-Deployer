
import os
import shutil
from datetime import datetime


def create():

    src="Core"

    dst=f"Core/runtime/snapshots/{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    os.makedirs(dst,exist_ok=True)

    shutil.copytree(
        src,
        dst,
        dirs_exist_ok=True
    )

    return dst


