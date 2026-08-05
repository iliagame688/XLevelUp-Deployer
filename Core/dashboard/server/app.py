from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from Core.dashboard import dashboard
from Core.watcher.intelligence import scan
from Core.deploy.agent import run


class Handler(BaseHTTPRequestHandler):

    def response(self,data):

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "application/json"
        )
        self.end_headers()

        self.wfile.write(
            json.dumps(
                data,
                indent=4
            ).encode()
        )


    def do_GET(self):

        if self.path=="/":

            self.response({

                "engine":"XDEPLOY v11",
                "status":"ONLINE",
                "dashboard":dashboard()

            })


        elif self.path=="/status":

            self.response({

                "dashboard":dashboard(),

                "workspace":scan(),

                "deploy":run()

            })


        else:

            self.response({

                "error":"NOT_FOUND"

            })



def start():

    server=HTTPServer(
        ("0.0.0.0",8080),
        Handler
    )


    print(
    """
╔══════════════════════════════╗
║   XDEPLOY v11 DASHBOARD      ║
║   http://localhost:8080      ║
╚══════════════════════════════╝
"""
    )


    server.serve_forever()



if __name__=="__main__":
    start()

