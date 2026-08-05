from http.server import BaseHTTPRequestHandler,HTTPServer
import json

from Core.dashboard.center import dashboard
from Core.events.stream import get_events
from Core.control.actions import deploy_action,rollback_action


HTML="""
<!DOCTYPE html>
<html>
<head>

<title>XDEPLOY v24</title>

<style>

body{
background:#0b0f14;
color:#00ff99;
font-family:monospace;
padding:30px;
}

.box{

border:1px solid #00ff99;
padding:20px;
margin:15px;
border-radius:10px;

}

button{

background:#00ff99;
border:0;
padding:12px;
margin:5px;
font-weight:bold;

}

pre{

color:white;

}

</style>

</head>

<body>


<h1>
XLEVELUP CONTROL CENTER
<br>
XDEPLOY v24
</h1>


<div class="box">

<h2>Status</h2>

<pre id="status">
Loading...
</pre>

</div>


<div class="box">

<button onclick="fetch('/deploy')">
DEPLOY
</button>


<button onclick="fetch('/rollback')">
ROLLBACK
</button>


<button onclick="load()">
REFRESH
</button>

</div>


<div class="box">

<h2>Events</h2>

<pre id="events">
</pre>

</div>



<script>

function load(){

fetch('/status')
.then(r=>r.json())
.then(x=>{

document.getElementById(
"status"
).innerHTML=
JSON.stringify(x,null,2)

})


fetch('/events')
.then(r=>r.json())
.then(x=>{

document.getElementById(
"events"
).innerHTML=
JSON.stringify(x,null,2)

})

}


setInterval(load,3000)

load()

</script>


</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):


    def send(self,data):

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

            self.send_response(200)

            self.send_header(
            "Content-Type",
            "text/html"
            )

            self.end_headers()

            self.wfile.write(
            HTML.encode()
            )


        elif self.path=="/status":

            self.send(
            dashboard()
            )


        elif self.path=="/events":

            self.send(
            get_events()
            )


        elif self.path=="/deploy":

            self.send(
            deploy_action()
            )


        elif self.path=="/rollback":

            self.send(
            rollback_action()
            )



def start():

    server=HTTPServer(
    ("0.0.0.0",8080),
    Handler
    )


    print(
    "XDEPLOY WEB CENTER :8080"
    )


    server.serve_forever()



