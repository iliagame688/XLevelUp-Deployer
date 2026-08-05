
import json
from pathlib import Path



class UploadHistory:


    def save(self, data):

        Path(
            "upload_history.json"
        ).write_text(

            json.dumps(
                data,
                indent=4
            )

        )



history = UploadHistory()

