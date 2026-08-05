from Core.commands.registry import registry


from Core.commands.actions import (
    status,
    deploy,
    logs,
    boot
)



registry.register(
    "xstatus",
    status
)

registry.register(
    "xdeploy",
    deploy
)

registry.register(
    "xlogs",
    logs
)

registry.register(
    "xboot",
    boot
)



class CommandRouter:



    def execute(
        self,
        command
    ):


        action = registry.get(
            command
        )


        if not action:

            return {

                "error":
                    "COMMAND_NOT_FOUND"

            }



        return action()




router = CommandRouter()
