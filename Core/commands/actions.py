from Core.control.controller import control

from Core.control.state import state



def status():

    return {

        "engine":
            state.snapshot(),

        "message":
            "XCONTROL ONLINE"

    }




def deploy():

    return {

        "action":
            "DEPLOY",

        "status":
            "READY"

    }




def logs():

    return {

        "action":
            "LOGS",

        "status":
            "OPEN"

    }




def boot():

    return control.boot()
