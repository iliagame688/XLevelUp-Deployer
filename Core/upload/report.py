

class UploadReport:


    def build(self, result):


        return {

            "operation":

                "UPLOAD",


            "files":

                result["files"],


            "status":

                result["status"]

        }




report = UploadReport()

