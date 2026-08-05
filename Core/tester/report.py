

class TestReport:


    def build(self, results):


        passed = sum(

            1 for x in results.values()

            if x

        )


        total = len(results)



        return {

            "passed":

                passed,


            "total":

                total,


            "ready":

                passed == total,


            "details":

                results

        }




report = TestReport()

