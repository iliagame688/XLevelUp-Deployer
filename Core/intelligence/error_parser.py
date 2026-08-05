import re


class ErrorParser:


    def parse(self, error):


        result = {

            "raw":
                error,

            "file":
                None,

            "line":
                None,

            "type":
                "UNKNOWN"

        }


        file_match = re.search(
            r'File "(.+?)", line (\d+)',
            error
        )


        if file_match:


            result["file"] = file_match.group(1)

            result["line"] = file_match.group(2)



        if "ModuleNotFoundError" in error:

            result["type"] = "MISSING_MODULE"


        elif "ImportError" in error:

            result["type"] = "IMPORT_ERROR"


        elif "TypeError" in error:

            result["type"] = "TYPE_ERROR"


        return result




parser = ErrorParser()
