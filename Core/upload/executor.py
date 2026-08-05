

from Core.upload.engine import upload


class UploadExecutor:


    def run(self, workspace):


        return upload.upload(
            workspace
        )




executor = UploadExecutor()

