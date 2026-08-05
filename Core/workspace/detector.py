
class ProjectDetector:



    def detect(self, files):


        result = {


            "type":
                "UNKNOWN",


            "confidence":
                0

        }



        names = set(files)



        if (
            "requirements.txt"
            in names
        ):


            result = {

                "type":
                    "PYTHON",

                "confidence":
                    90

            }



        elif (
            "package.json"
            in names
        ):


            result = {


                "type":
                    "NODE",

                "confidence":
                    90

            }



        elif (
            "Dockerfile"
            in names
        ):


            result = {


                "type":
                    "DOCKER",

                "confidence":
                    95

            }



        return result





detector = ProjectDetector()
