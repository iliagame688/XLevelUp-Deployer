import os
import shutil
import datetime
import ast


TARGETS=[
"Core/pipeline/deploy.py",
"Core/runtime/snapshots/20260806_014843/Core/pipeline/deploy.py"
]


def backup(path):

    if os.path.exists(path):

        b=path+".backup_fix_"+datetime.datetime.now().strftime("%H%M%S")

        shutil.copy2(path,b)

        return b



def inspect(path,line=25):

    if not os.path.exists(path):
        return []

    with open(path,"r",encoding="utf-8") as f:
        data=f.readlines()

    start=max(0,line-8)
    end=min(len(data),line+8)

    return [
        f"{i+1}: {data[i].rstrip()}"
        for i in range(start,end)
    ]



def validate(path):

    try:

        with open(path,"r",encoding="utf-8") as f:

            ast.parse(f.read())

        return True,None


    except Exception as e:

        return False,str(e)



def repair(path):

    print("\nTARGET:",path)


    print("\n--- CONTEXT ---")

    for x in inspect(path):
        print(x)


    ok,error=validate(path)


    if ok:

        return {
        "status":"OK",
        "file":path
        }


    backup_file=backup(path)


    return {

    "status":"NEEDS_PATCH",

    "file":path,

    "backup":backup_file,

    "error":error

    }



def run():

    results=[]

    for t in TARGETS:

        results.append(
            repair(t)
        )


    return results



if __name__=="__main__":

    print(run())

