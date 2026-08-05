from pathlib import Path


IGNORE = [

    "__pycache__",

    ".pyc",

    ".tmp"

]


class UploadScanner:


    def scan(self, path):


        files = []


        for item in Path(path).rglob("*"):


            if not item.is_file():

                continue


            skip = False


            for rule in IGNORE:


                if rule in item.name or rule in str(item):

                    skip = True


            if not skip:

                files.append(
                    str(item)
                )


        return files




scanner = UploadScanner()

