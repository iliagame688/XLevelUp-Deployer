
class CleanupAnalyzer:


    def analyze(self, data):


        return {

            "safe_count":
                len(data["safe"]),

            "review_count":
                len(data["review"]),

            "protected_count":
                len(data["protected"])

        }




analyzer = CleanupAnalyzer()
