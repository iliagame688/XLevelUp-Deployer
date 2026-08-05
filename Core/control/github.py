import json

from pathlib import Path
from datetime import datetime


STATE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/github.json"
)



class GitHubManager:


    def save_state(
        self,
        data
    ):

        STATE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        STATE.write_text(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )



    def check_token(
        self,
        token
    ):

        # فعلاً لایه اتصال آماده است
        # اتصال واقعی API در مرحله بعد اضافه می‌شود

        result = {

            "time":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "connected":
                False,

            "account":
                None,

            "permission":
                None,

            "status":
                "WAITING_API"

        }


        if token.startswith(
            "ghp_"
        ) or token.startswith(
            "github_pat_"
        ):

            result["status"] = "TOKEN_ACCEPTED"


        else:

            result["status"] = "INVALID_TOKEN"



        self.save_state(
            result
        )


        return result




    def status(self):

        if not STATE.exists():

            return {
                "status":
                    "NOT_CONNECTED"
            }


        return json.loads(
            STATE.read_text(
                encoding="utf-8"
            )
        )



github = GitHubManager()
