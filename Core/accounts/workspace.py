class WorkspaceManager:



    def add(
        self,
        account,
        path
    ):


        account.workspaces.append(
            path
        )


        return {

            "account":
                account.name,

            "workspace":
                path

        }



workspace = WorkspaceManager()
