import os
import shutil
from datetime import datetime


TARGET="Core/data/last_deploy.json"


if not os.path.exists(TARGET):
    print("REPORT FILE NOT FOUND")
    exit()



backup = TARGET + ".backup_" + datetime.now().strftime("%H%M%S")


shutil.copy(
    TARGET,
    backup
)


print(
    "BACKUP:",
    backup
)



print("""
XDEPLOY REPORT PATCH READY

Next deploy will store:

PUSH:
{
 status: SUCCESS / RECOVERED / FAILED,
 mode: SMART_PUSH
}

instead of raw git output.
""")

