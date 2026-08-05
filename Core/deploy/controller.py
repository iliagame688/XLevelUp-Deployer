from datetime import datetime


def deploy():

    return {

    "deploy":"READY",

    "engine":"XDEPLOY v21",

    "time":str(datetime.now())

    }



def rollback():

    return {

    "rollback":"READY",

    "engine":"XDEPLOY v21"

    }
