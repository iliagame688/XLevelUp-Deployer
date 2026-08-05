
from pathlib import Path


class GitAnalyzer:


    def analyze(self, path):


        files = []


        root = Path(path)


        if root.exists():


            for item in root.rglob("*"):

                if item.is_file():

                    files.append(
                        str(item.relative_to(root))
                    )


        return {

            "files":
                len(files),

            "sample":
                files[:5]

        }




analyzer = GitAnalyzer()
