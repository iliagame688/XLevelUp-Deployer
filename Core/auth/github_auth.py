from pathlib import Path
import json
import getpass


VAULT = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/vault.json"
)


class GithubAuth:

    def setup(self):

        if VAULT.exists():

            try:
                data = json.loads(
                    VAULT.read_text()
                )

                if data.get("token"):
                    return {
                        "status":"READY",
                        "source":"VAULT"
                    }

            except:
                pass


        print(
            "╭──────── XLEVELUP GITHUB AUTH ────────╮"
        )

        token = getpass.getpass(
            "GitHub Token: "
        )


        if not token:
            return {
                "status":"FAILED"
            }


        VAULT.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        VAULT.write_text(
            json.dumps(
                {
                    "token":token
                },
                indent=4
            )
        )


        return {
            "status":"READY"
        }


github_auth = GithubAuth()
