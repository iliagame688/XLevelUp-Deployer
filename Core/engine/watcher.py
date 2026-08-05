from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from engine.events import save_event
from engine.state import update


class XDeployHandler(FileSystemEventHandler):

    def handle(self, event_type, path):

        event = save_event(
            event_type,
            path
        )

        update(event)

        print(
            f"[{event_type}] {path}"
        )


    def on_created(self, event):

        if not event.is_directory:
            self.handle(
                "CREATED",
                event.src_path
            )


    def on_modified(self, event):

        if not event.is_directory:
            self.handle(
                "MODIFIED",
                event.src_path
            )


    def on_deleted(self, event):

        if not event.is_directory:
            self.handle(
                "DELETED",
                event.src_path
            )



def start_watch(path):

    print("""
╭──────────────────────────╮
│ XDEPLOY WATCHER PRO      │
╰──────────────────────────╯
""")

    print("WATCHING:")
    print(path)


    observer = Observer()

    observer.schedule(
        XDeployHandler(),
        path,
        recursive=True
    )

    observer.start()


    try:

        while True:
            pass

    except KeyboardInterrupt:

        observer.stop()


    observer.join()
