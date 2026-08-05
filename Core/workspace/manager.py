from Core.workspace.config import (
    save,
    load
)



class WorkspaceManager:



    def add(
        self,
        name,
        path
    ):


        data = load()


        item = {

            "name":
                name,

            "path":
                path,

            "status":
                "READY"

        }


        data["workspaces"].append(
            item
        )


        if not data["active"]:

            data["active"] = name



        save(data)


        return item




    def activate(
        self,
        name
    ):


        data = load()


        for item in data["workspaces"]:

            if item["name"] == name:

                data["active"] = name

                save(data)

                return {

                    "status":
                        "ACTIVE",

                    "workspace":
                        name

                }



        return {

            "status":
                "NOT_FOUND"

        }





    def list(self):

        return load()




workspace = WorkspaceManager()
