import os
import json
import subprocess
from pathlib import Path
from getpass import getpass


ROOT = Path("/storage/emulated/0/XLevelUp-Deployer")

VAULT = ROOT / "Core" / "security" / "github_token.json"


class GitAuth:

    def git(self, args):

        return subprocess.run(
            ["git"] + args,
            cwd=ROOT,
            capture_output=True,
            text=True
        )


    def save_token(self, token):

        VAULT.parent.mkdir(
            exist_ok=True
        )

        VAULT.write_text(
            json.dumps(
                {
                    "token": token
                },
                indent=4
            )
        )


    def load_token(self):

        if not VAULT.exists():
            return None

        try:
            data=json.loads(
                VAULT.read_text()
            )

            return data.get(
                "token"
            )

        except:
            return None



    def request_token(self):

        print()
        print(
            "╭──────── GITHUB AUTH ────────╮"
        )

        print(
            "🔐 INPUT GITHUB TOKEN:"
        )

        token=getpass(
            "TOKEN > "
        )

        if not token:
            raise Exception(
                "TOKEN EMPTY"
            )


        self.save_token(
            token
        )


        print(
            "✓ TOKEN SAVED"
        )

        return token



    def ensure_identity(self):

        self.git(
            [
                "config",
                "user.name",
                "iliagame688"
            ]
        )


        self.git(
            [
                "config",
                "user.email",
                "iliagame688@users.noreply.github.com"
            ]
        )



    def setup_remote(self):

        remote=self.git(
            [
                "remote",
                "-v"
            ]
        )


        if "origin" not in remote.stdout:

            self.git(
                [
                    "remote",
                    "add",
                    "origin",
                    "https://github.com/iliagame688/XLevelUp-Deployer.git"
                ]
            )



    def authenticate(self):

        token=self.load_token()


        if not token:

            token=self.request_token()


        self.ensure_identity()

        self.setup_remote()


        return token



auth = GitAuth()
