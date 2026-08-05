
from Core.events.stream import push
from Core.deploy.controller import deploy,rollback
from Core.workspace.manager import set_workspace



def deploy_action():

    result=deploy()

    push(
        "DEPLOY",
        result
    )

    return result



def rollback_action():

    result=rollback()

    push(
        "ROLLBACK",
        result
    )

    return result



def workspace_action(path):

    result=set_workspace(path)

    push(
        "WORKSPACE_CHANGE",
        result
    )

    return result

