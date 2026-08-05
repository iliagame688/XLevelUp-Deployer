
class HealthAnalyzer:



    def analyze(self, results):


        failed = [

            item

            for item in results

            if item["status"] == "FAILED"

        ]



        return {


            "total":

                len(results),


            "passed":

                len(results)
                -
                len(failed),


            "failed":

                len(failed),


            "status":

                "ONLINE"

                if not failed

                else

                "DEGRADED"

        }




health = HealthAnalyzer()
