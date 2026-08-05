SERVICES = {}


def register(name, status="READY"):

    SERVICES[name] = {

        "status": status

    }



def update(name, status):

    if name in SERVICES:

        SERVICES[name]["status"] = status

    else:

        register(
            name,
            status
        )



def all_services():

    return SERVICES
