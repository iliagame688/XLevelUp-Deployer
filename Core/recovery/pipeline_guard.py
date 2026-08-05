
import os
import ast
import shutil
import datetime



BROKEN=[]



def check_file(path):

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            ast.parse(
                f.read()
            )


        return True


    except Exception as e:


        BROKEN.append({

            "file":path,

            "error":str(e)

        })


        return False




def scan(root="."):


    BROKEN.clear()


    for base,dirs,files in os.walk(root):


        if ".git" in base:
            continue


        for file in files:


            if file.endswith(".py"):

                check_file(
                os.path.join(
                base,
                file
                )
                )



    return BROKEN




def quarantine(path):


    if os.path.exists(path):

        backup=path+".broken_"+datetime.datetime.now().strftime(
            "%H%M%S"
        )


        shutil.move(
            path,
            backup
        )


        return backup



    return None



