from pathlib import Path

from Core.bootstrap.report import save



class BootstrapManager:



    def __init__(self):

        self.created = []
        self.updated = []
        self.skipped = []



    def check_file(
        self,
        path,
        content=None
    ):


        file = Path(path)


        if file.exists():


            if content is not None:

                old = file.read_text(
                    encoding="utf-8"
                )


                if old != content:

                    file.write_text(
                        content,
                        encoding="utf-8"
                    )

                    self.updated.append(
                        str(file)
                    )

                else:

                    self.skipped.append(
                        str(file)
                    )


            return "EXISTS"



        file.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        if content is not None:

            file.write_text(
                content,
                encoding="utf-8"
            )


        self.created.append(
            str(file)
        )


        return "CREATED"




    def summary(self):

        result = {

            "created":
                self.created,

            "updated":
                self.updated,

            "skipped":
                self.skipped

        }


        save(result)


        return result




bootstrap = BootstrapManager()
