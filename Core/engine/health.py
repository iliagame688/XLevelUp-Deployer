from Core.engine.registry import all_services



def check():

    services = all_services()


    failed = []


    for name, data in services.items():

        if data["status"] in [
            "ERROR",
            "OFFLINE"
        ]:

            failed.append(name)



    return {

        "health":

            "GOOD"
            if not failed
            else "WARNING",


        "services":

            services,


        "errors":

            failed

    }
