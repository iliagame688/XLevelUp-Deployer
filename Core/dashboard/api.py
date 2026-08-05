
from Core.dashboard.app import dashboard

from Core.dashboard.state import state



def start_dashboard():


    state.online()

    state.set_mode(
        "CONTROL_CENTER"
    )


    dashboard.start()


    return state.snapshot()




def run_dashboard(*args, **kwargs):

    return start_dashboard()




def dashboard_status():

    return state.snapshot()




def stop_dashboard():

    state.status = "OFFLINE"

    return {

        "status":
            "STOPPED"

    }

