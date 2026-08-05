from pathlib import Path



class CleanupScanner:


    def scan(self, path):

        root = Path(path)


        result = {

            "safe": [],

            "review": [],

            "protected": []

        }


        for item in root.rglob("*"):


            if not item.is_file():

                continue


            name = item.name


            if name.endswith(".pyc"):

                result["safe"].append(
                    str(item)
                )


            elif name.endswith(".bak"):

                result["safe"].append(
                    str(item)
                )


            else:

                result["protected"].append(
                    str(item)
                )


        return result




scanner = CleanupScanner()
