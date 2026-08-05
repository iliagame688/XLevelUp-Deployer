from Core.deploy.real_engine import real_engine


REAL_ENABLED = True


def dispatch(path):

    if REAL_ENABLED:

        return real_engine.run()


    return {
        "engine":"XDEPLOY",
        "status":"SAFE_TEST",
        "mode":"TEST"
    }
