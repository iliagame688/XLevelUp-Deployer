import os
import re


IGNORE_FILES=[
    "github_auth.json",
    "guard.py",
    "xdeploy_v16_git_bridge_bootstrap.sh",
    "xdeploy_v16_1_firewall_patch.sh"
]


IGNORE_DIRS=[
    ".git",
    "__pycache__",
    "Core/runtime",
    "Core/archive"
]


REAL_PATTERNS=[

    r"ghp_[A-Za-z0-9]{30,}",

    r"github_pat_[A-Za-z0-9_]{30,}",

    r"-----BEGIN PRIVATE KEY-----",

    r"AKIA[0-9A-Z]{16}"

]


def ignored(path):

    for d in IGNORE_DIRS:

        if d in path:

            return True


    for f in IGNORE_FILES:

        if path.endswith(f):

            return True


    return False



def scan():

    found=[]


    for root,dirs,files in os.walk("."):


        if ignored(root):

            dirs[:]=[]

            continue



        for file in files:


            path=os.path.join(
                root,
                file
            )


            if ignored(path):

                continue



            if not file.endswith(
                (
                ".py",
                ".json",
                ".env",
                ".txt"
                )
            ):

                continue



            try:

                data=open(
                    path,
                    errors="ignore"
                ).read()



                for p in REAL_PATTERNS:

                    if re.search(
                        p,
                        data
                    ):

                        found.append(path)

                        break


            except:

                pass



    return found



if __name__=="__main__":

    print(scan())

