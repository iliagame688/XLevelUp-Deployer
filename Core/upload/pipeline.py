from Core.git.control import git_control
import subprocess

from Core.upload.commit import (
    save,
    generate_message
)



class UploadPipeline:



    def detect_changes(self, path):

        try:

            git_result = git_control.execute(
                path,
                [
                    "status",
                    "--short"
                ]
            )


            if git_result.get("status") == "SKIPPED":

                return []


            result = git_result.get(
                "stdout",
                ""
            )


            return [
                x[3:]
                for x in result.splitlines()
                if x.strip()
            ]


        except Exception:

            return []




    def prepare(self, path):

        files = self.detect_changes(
            path
        )


        data = {

            "files":
                files,

            "count":
                len(files),

            "commit":
                generate_message(
                    files
                ),

            "status":
                "READY"
        }



        if not files:

            data["status"] = "NO_CHANGES"



        save(
            data
        )


        return data




pipeline = UploadPipeline()
