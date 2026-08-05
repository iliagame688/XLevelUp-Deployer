from pathlib import Path

from Core.cleanup.backup import backup

from Core.cleanup.history import history



class CleanupExecutor:


    def execute(self, files, root):


        backup_data = backup.create(
            files,
            root
        )


        removed = []


        for file in files:

            path = Path(file)


            if path.exists():

                path.unlink()

                removed.append(
                    str(path)
                )


        result = {


            "removed":
                removed,


            "backup":
                backup_data

        }


        history.save(
            result
        )


        return result




executor = CleanupExecutor()
