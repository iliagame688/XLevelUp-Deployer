from http.server import HTTPServer,BaseHTTPRequestHandler

from Core.dashboard.control_plane import (
    dashboard,
    deploy,
    rollback
)

import json


class API(BaseHTTPRequestHandler):


    def send(self,data):

        self.send_response(200)

        self.send_header(
            "Content-Type",
            "application/json"
        )

        self.end_headers()

        self.wfile.write(
            json.dumps(data).encode()
        )



    def do_GET(self):

        if self.path=="/":

            self.send(
                dashboard()
            )


        elif self.path=="/deploy":

            self.send(
                deploy()
            )


        elif self.path=="/rollback":

            self.send(
                rollback()
            )


server=HTTPServer(
    ("0.0.0.0",8787),
    API
)


print(
"XDEPLOY API :8787"
)


server.serve_forever()

