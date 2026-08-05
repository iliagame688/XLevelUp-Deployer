from pathlib import Path


class GitScanner:


    def scan(self, path):


        root = Path(path)


        return {

            "path":
                str(root),

            "exists":
                root.exists(),

            "git":
                (root / ".git").exists()

        }



scanner = GitScanner()
