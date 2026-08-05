
from http.server import BaseHTTPRequestHandler,HTTPServer
import json

from Core.dashboard.center import dashboard
from Core.control.actions import (
deploy_action,
rollback_action
)

from Core.events.stream import get_events



class Handler(BaseHTTPRequestHandler):


    def send_json(self,data):

        self.send_response(200)

        self.send_header(
        "Content-Type",
        "application/json"
        )

        self.end_headers()

        self.wfile.write(
            json.dumps(data,indent=4).encode()
        )



    def do_GET(self):

        if self.path=="/":

            self.send_json(
                dashboard()
            )


        elif self.path=="/events":

            self.send_json(
                get_events()
            )


        elif self.path=="/deploy":

            self.send_json(
                deploy_action()
            )


        elif self.path=="/rollback":

            self.send_json(
                rollback_action()
            )


        else:

            self.send_json(
            {
            "error":"NOT_FOUND"
            }
            )




def start():

    server=HTTPServer(
        ("0.0.0.0",8080),
        Handler
    )

    print(
    """
╔════════════════════════════╗
║ XDEPLOY v22 SERVER         ║
║ PORT 8080                  ║
╚════════════════════════════╝
    """
    )


    server.serve_forever()



if __name__=="__main__":

    start()

