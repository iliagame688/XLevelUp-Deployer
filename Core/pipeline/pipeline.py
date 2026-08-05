from Core.pipeline.stages import stage

from Core.pipeline.report import PipelineReport



class DeployPipeline:



    def __init__(self):

        self.report = PipelineReport()



    def run(self, project):


        steps = [


            (
                "ACCOUNT_CHECK",
                "SUCCESS"
            ),


            (
                "WORKSPACE_SCAN",
                "SUCCESS"
            ),


            (
                "PROJECT_ANALYSIS",
                "SUCCESS"
            ),


            (
                "DEPLOY",
                "RUNNING"
            ),


            (
                "HEALTH_CHECK",
                "WAITING"
            )

        ]



        for name,status in steps:


            self.report.add(

                stage(

                    name,

                    status,

                    project

                )

            )



        return self.report.result()




pipeline = DeployPipeline()
