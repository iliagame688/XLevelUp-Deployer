import ast
import os


def scan_file(path):

    try:
        with open(path,"r",encoding="utf-8") as f:
            code=f.read()

        ast.parse(code)

        return {
            "file":path,
            "status":"OK"
        }


    except SyntaxError as e:

        return {

            "file":path,

            "status":"BROKEN",

            "line":e.lineno,

            "error":str(e)

        }



def scan_project(root="Core"):

    result=[]

    for base,dirs,files in os.walk(root):

        for file in files:

            if file.endswith(".py"):

                result.append(
                    scan_file(
                    os.path.join(base,file)
                    )
                )


    return result

