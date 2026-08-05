
from pathlib import Path
import subprocess
import json
import getpass
from datetime import datetime


ROOT = Path(
    "/storage/emulated/0/XLevelUp-Deployer"
)

VAULT = ROOT / "Core/data/real_vault.json"



class RealDeployEngine:


    def load_vault(self):

        if not VAULT.exists():
            return {}

        try:
            return json.loads(
                VAULT.read_text(
                    encoding="utf-8"
                )
            )

        except:
            return {}



    def save_vault(self,data):

        VAULT.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        VAULT.write_text(
            json.dumps(
                data,
                indent=4
            ),
            encoding="utf-8"
        )



    def auth(self):

        data = self.load_vault()


        if data.get("token"):

            return {
                "status":"READY"
            }



        print()

        print(
            "╭──────── XLEVELUP GITHUB AUTH ────────╮"
        )


        token = getpass.getpass(
            "GitHub Token: "
        )


        if not token:

            return {
                "status":"FAILED",
                "reason":"NO_TOKEN"
            }


        repo = input(
            "Repository URL: "
        )


        branch = input(
            "Branch [main]: "
        )


        if not branch:
            branch = "main"


        data = {

            "token": token,

            "repo": repo,

            "branch": branch,

            "created":
                str(datetime.now())

        }


        self.save_vault(
            data
        )


        print(
            "✓ AUTH SAVED"
        )


        print(
            "╰──────────────────────────────────────╯"
        )


        return {
            "status":"READY"
        }



    def git(self,args):

        return subprocess.run(
            [
                "git",
                "-C",
                str(ROOT)
            ]
            +
            args,

            capture_output=True,

            text=True
        )



    def run(self):


        auth = self.auth()


        if auth["status"] != "READY":

            return {

                "engine":"XDEPLOY",

                "status":
                    "AUTH_FAILED",

                "mode":
                    "REAL"

            }



        result = {

            "engine":
                "XDEPLOY",

            "mode":
                "REAL",

            "steps":[]

        }



        status = self.git(
            [
                "status",
                "--short"
            ]
        )


        files = status.stdout.splitlines()



        result["steps"].append({

            "name":
                f"FILES {len(files)}"

        })



        self.git(
            [
                "add",
                "."
            ]
        )


        commit = self.git(
            [
                "commit",
                "-m",
                "XLEVELUP AUTO DEPLOY"
            ]
        )



        result["steps"].append({

            "name":
                "COMMIT CREATED"

        })



        push = self.git(
            [
                "push"
            ]
        )



        if push.returncode == 0:

            result["status"] = "SUCCESS"

            result["steps"].append({

                "name":
                    "PUSH COMPLETE"

            })

        else:

            result["status"] = "PUSH_FAILED"

            result["error"] = push.stderr



        return result




real_engine = RealDeployEngine()

