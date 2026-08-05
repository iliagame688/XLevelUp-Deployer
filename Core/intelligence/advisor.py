from Core.intelligence.error_parser import parser

from Core.intelligence.classifier import classifier



class RepairAdvisor:



    def analyze(self, error):


        parsed = parser.parse(
            error
        )


        result = classifier.classify(
            parsed
        )


        return {


            "location":
                {

                "file":
                    parsed["file"],

                "line":
                    parsed["line"]

                },


            "type":
                parsed["type"],


            "cause":
                result["cause"]

        }




advisor = RepairAdvisor()
