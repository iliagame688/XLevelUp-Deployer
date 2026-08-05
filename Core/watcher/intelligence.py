

import os


def scan():


    result=[]


    for root,dirs,files in os.walk("."):


        if ".git" in root:

            continue


        for f in files:

            result.append(
            os.path.join(root,f)
            )


    return {


    "files":len(result),

    "status":"WATCHING"


    }



