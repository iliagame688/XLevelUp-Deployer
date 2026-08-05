import os
from Core.workspace.manager import get_workspace


def scan():

    cfg=get_workspace()

    if not cfg:
        return []


    root=cfg["path"]

    ignore=cfg.get("ignore",[])

    result=[]


    for base,dirs,files in os.walk(root):

        dirs[:]=[
            d for d in dirs
            if d not in ignore
        ]


        for f in files:

            if f.endswith(".py"):

                result.append(
                    os.path.join(base,f)
                )


    return result


if __name__=="__main__":

    print(
        {
        "files":len(scan()),
        "status":"WATCHING"
        }
    )
