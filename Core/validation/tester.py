import importlib

from Core.validation.report import summary



class ModuleTester:



    def test(
        self,
        module
    ):

        checks = []


        try:

            importlib.import_module(
                module
            )

            checks.append(
                "IMPORT ✓"
            )


            status = "READY"



        except Exception as e:


            checks.append(
                "ERROR: "
                +
                str(e)
            )


            status = "FAILED"



        return summary(

            module,

            checks,

            status

        )




tester = ModuleTester()
