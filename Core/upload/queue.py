
class UploadQueue:


    def create(self, files):


        return {


            "total":
                len(files),


            "files":
                files,


            "uploaded":
                0

        }





queue = UploadQueue()

