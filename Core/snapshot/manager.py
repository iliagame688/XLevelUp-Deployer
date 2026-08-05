import os
import shutil
from datetime import datetime



BASE="Core/runtime/snapshots"



def create():


    os.makedirs(
    BASE,
    exist_ok=True
    )


    name=datetime.now().strftime(
    "%Y%m%d_%H%M%S"
    )


    target=os.path.join(
    BASE,
    name
    )


    os.makedirs(target)


    return {

    "snapshot":target,

    "status":"CREATED"

    }

