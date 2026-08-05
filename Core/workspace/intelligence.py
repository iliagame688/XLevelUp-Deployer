from Core.workspace.scanner import scanner

from Core.workspace.detector import detector

from Core.dashboard.live.event_bus import bus



class WorkspaceAI:


    def analyze(self, path):


        bus.emit(
            "Workspace analysis started",
            "AI"
        )


        data = scanner.scan(
            path
        )


        project = detector.detect(
            data["files"]
        )


        bus.emit(
            "Workspace analysis completed",
            "SUCCESS"
        )


        return {


            "workspace":
                data,


            "project":
                project

        }




workspace_ai = WorkspaceAI()
