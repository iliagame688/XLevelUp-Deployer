from pathlib import Path
import shutil
from datetime import datetime



class BackupManager:


    def create(self, files, root):


        backup_dir = Path(root) / "cleanup_backup" / datetime.now().strftime("%Y%m%d_%H%M%S")


        backup_dir.mkdir(
            parents=True,
            exist_ok=True
        )


        saved = []


        for file in files:

            source = Path(file)


            if source.exists():

                target = backup_dir / source.name

                shutil.copy2(
                    source,
                    target
                )

                saved.append(
                    str(target)
                )


        return {

            "backup":
                str(backup_dir),

            "files":
                saved

        }



backup = BackupManager()
