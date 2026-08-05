import os
import py_compile


def scan():


    broken=[]


    for root,dirs,files in os.walk("."):


        if "runtime" in root:
            continue


        for f in files:


            if f.endswith(".py"):


                path=os.path.join(root,f)


                try:

                    py_compile.compile(
                    path,
                    doraise=True
                    )


                except Exception as e:

                    broken.append({

                    "file":path,

                    "error":str(e)

                    })


    return {

    "compile":

    "PASS" if not broken else "FAILED",

    "errors":broken

    }

