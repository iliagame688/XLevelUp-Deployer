

from Core.pipeline.autonomous import (
deploy,
rollback
)


def execute(action):

    if action=="deploy":

        return deploy()


    if action=="rollback":

        return rollback()


    return {

    "error":
    "UNKNOWN_ACTION"

    }

