class ErrorClassifier:


    def classify(self, data):


        rules = {


            "MISSING_MODULE":
                "Dependency or file missing",


            "IMPORT_ERROR":
                "Import structure problem",


            "TYPE_ERROR":
                "Function arguments mismatch"

        }


        return {

            "cause":
                rules.get(
                    data["type"],
                    "Unknown runtime issue"
                )

        }




classifier = ErrorClassifier()


# Compatibility API
# Supports old analyzer imports

def classify(data):

    return classifier.classify(data)

