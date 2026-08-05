from pathlib import Path


class FileIndexer:


    def scan(self, path):

        files = []


        for item in Path(path).rglob("*"):

            if item.is_file():

                files.append({

                    "name":
                        item.name,

                    "size":
                        item.stat().st_size,

                    "path":
                        str(item)

                })


        return files



indexer = FileIndexer()
