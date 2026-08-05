import json
from pathlib import Path



class CleanupHistory:


    def save(self, data):


        file = Path(
            "cleanup_history.json"
        )


        file.write_text(
            json.dumps(
                data,
                indent=4
            )
        )



history = CleanupHistory()
