from Core.preflight.checker import checker
from Core.dashboard.live.event_bus import bus
from Core.git.guard import guard
from Core.workspace.scanner import scan

from Core.upload.pipeline import pipeline

from Core.git.commit_engine import commit_engine

from Core.git.push_engine import push_engine

from Core.deploy.report import save






def deploy_event(message, level="INFO", progress=0):

    try:

        bus.emit(
            message,
            level,
            progress
        )

    except Exception:

        pass



class DeployOrchestrator:



    def run(self, path):


        result = {

            "engine":
                "XDEPLOY",

            "steps":
                []

        }


        deploy_event(
            "DEPLOY STARTED",
            "INFO",
            0
        )



        # Workspace

        deploy_event(
            "WORKSPACE SCAN",
            "RUNNING",
            10
        )


        workspace = scan(path)


        deploy_event(
            "WORKSPACE READY",
            "SUCCESS",
            25
        )


        result["steps"].append({

            "name":
                "WORKSPACE_SCAN",

            "status":
                "DONE",

            "data":
                workspace

        })



        # Changes

        deploy_event(
            "CHANGE DETECT",
            "RUNNING",
            35
        )


        files = pipeline.detect_changes(
            path
        )


        result["steps"].append({

            "name":
                "CHANGE_DETECT",

            "files":
                files,

            "count":
                len(files)

        })



        deploy_event(
            "CHANGE DETECT READY",
            "SUCCESS",
            50
        )


        if not files:


            deploy_event(
                "NO CHANGES - SAFE TEST COMPLETE",
                "SUCCESS",
                100
            )


            result["steps"].append({

                "name":
                    "TEST_MODE",

                "status":
                    "SKIPPED",

                "reason":
                    "NO CHANGES"

            })


            result["final"] = {

                "status":
                    "SUCCESS",

                "mode":
                    "TEST",

                "message":
                    "SAFE DEPLOY FINISHED"

            }


            deploy_event("VERIFY DEPLOY","RUNNING",85)

        deploy_event("DEPLOY FINISHED","SUCCESS",100)

        return save(result)





        # Commit


        commit = commit_engine.run(

            path,

            files

        )


        result["steps"].append({

            "name":
                "COMMIT",

            "data":
                commit

        })



        if commit.get("status") != "SUCCESS":


            result["final"] = {

                "status":
                    "COMMIT_FAILED"

            }


            return save(result)





        # Push


        push = push_engine.push(
            path
        )


        result["steps"].append({

            "name":
                "PUSH",

            "data":
                push

        })



        result["final"] = {

            "status":
                push.get(
                    "status",
                    "UNKNOWN"
                )

        }


        return save(result)





deploy_engine = DeployOrchestrator()
