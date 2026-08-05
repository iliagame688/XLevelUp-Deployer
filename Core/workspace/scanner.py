from pathlib import Path



class WorkspaceScanner:


    def scan(self, path):


        root = Path(path)


        files = []


        if root.exists():


            for item in root.rglob("*"):

                if item.is_file():

                    files.append(
                        item.name
                    )


        return {


            "path":
                str(root),


            "files":
                files,

            "count":
                len(files)

        }




scanner = WorkspaceScanner()


# Compatibility API
# Supports old collector imports

def scan(path):

    return scanner.scan(path)


