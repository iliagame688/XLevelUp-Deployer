import importlib

from datetime import datetime


from Core.integrity.modules import MODULES

from Core.integrity.report import save



class IntegrityChecker:



    def run(self):


        results = []


        for module in MODULES:


            item = {

                "module":
                    module,

                "status":
                    "OK"

            }


            try:

                importlib.import_module(
                    module
                )


            except Exception as e:


                item["status"] = "ERROR"

                item["error"] = str(e)



            results.append(
                item
            )



        report = {


            "time":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),


            "modules":
                results

        }



        save(report)


        return report




checker = IntegrityChecker()
