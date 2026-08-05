from Core.optimizer.indexer import indexer

from Core.optimizer.analyzer import analyzer



class OptimizerReport:


    def generate(self, path):


        files = indexer.scan(path)


        return analyzer.analyze(
            files
        )




optimizer_report = OptimizerReport()
