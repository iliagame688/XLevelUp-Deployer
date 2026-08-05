
from Core.cleanup.scanner import scanner

from Core.cleanup.analyzer import analyzer



class CleanupReport:


    def generate(self, path):


        scan = scanner.scan(path)


        result = analyzer.analyze(
            scan
        )


        return {


            "summary":
                result,


            "files":
                scan["safe"][:20]

        }




report = CleanupReport()
