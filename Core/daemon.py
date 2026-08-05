from engine.watcher import start_watch


def start_daemon(config):

    path = config.get(
        "watch_path"
    )

    if not path:

        print(
            "WORKSPACE NOT SET"
        )

        return


    start_watch(path)
