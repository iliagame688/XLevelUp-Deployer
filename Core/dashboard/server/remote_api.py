from http.server import HTTPServer,BaseHTTPRequestHandler
import json


from Core.remote.bridge import deploy,rollback
from Core.events.stream import emit,history



class API(BaseHTTPRequestHandler):


    def send_json(self,data):

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

        if self.path=="/deploy":

            r=deploy()

            emit(
            "DEPLOY",
            r
            )

            self.send_json(r)



        elif self.path=="/rollback":

            r=rollback()

            emit(
            "ROLLBACK",
            r
            )

            self.send_json(r)



        elif self.path=="/events":

            self.send_json(
            history()
            )


        else:

            self.send_json(
            {
            "engine":"XDEPLOY v12",
            "status":"ONLINE"
            }
            )



def start():

    print(
    """
╔══════════════════════════╗
║ XDEPLOY v12 API ONLINE  ║
║ PORT 8090               ║
╚══════════════════════════╝
"""
    )


    HTTPServer(
    ("0.0.0.0",8090),
    API
    ).serve_forever()



if __name__=="__main__":
    start()

