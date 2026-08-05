#!/data/data/com.termux/files/usr/bin/bash

set -e

PROJECT="/storage/emulated/0/XLevelUp-Deployer"

cd "$PROJECT"

echo "
╔══════════════════════════════════════╗
║          XDEPLOY v13                 ║
║       WEB CONTROL CENTER              ║
╚══════════════════════════════════════╝
"


echo "[1] Creating UI structure"

mkdir -p Core/dashboard/web


echo "[2] Creating Dashboard Server"


cat > Core/dashboard/web/server.py <<'PY'
from http.server import HTTPServer,BaseHTTPRequestHandler
import json
from urllib.parse import urlparse

from Core.dashboard import dashboard
from Core.watcher.intelligence import scan
from Core.remote.bridge import deploy,rollback
from Core.events.stream import history,emit



HTML="""

<!DOCTYPE html>

<html>

<head>

<title>XDEPLOY CONTROL</title>

<style>

body{
background:#0b0f14;
color:#00ff99;
font-family:monospace;
padding:30px;
}


.card{

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


<h1>XDEPLOY v13 CONTROL CENTER</h1>


<div class="card">

<h2>Status</h2>

<pre id="status">
Loading...
</pre>


</div>



<div class="card">


<button onclick="action('/deploy')">
DEPLOY
</button>


<button onclick="action('/rollback')">
ROLLBACK
</button>


</div>



<div class="card">


<h2>Events</h2>

<pre id="events">
</pre>


</div>



<script>


async function load(){

let s=await fetch('/status');

document.getElementById(
'status'
).innerHTML=
JSON.stringify(
await s.json(),
null,
4
);


let e=await fetch('/events');

document.getElementById(
'events'
).innerHTML=
JSON.stringify(
await e.json(),
null,
4
);


}


async function action(url){

await fetch(url);

load();

}


setInterval(load,3000);

load();


</script>


</body>

</html>

"""



class Handler(BaseHTTPRequestHandler):


    def send(self,data,ctype="application/json"):

        self.send_response(200)

        self.send_header(
        "Content-Type",
        ctype
        )

        self.end_headers()

        if isinstance(data,str):

            self.wfile.write(
            data.encode()
            )

        else:

            self.wfile.write(
            json.dumps(
            data,
            indent=4
            ).encode()
            )


    def do_GET(self):


        if self.path=="/":

            self.send(
            HTML,
            "text/html"
            )


        elif self.path=="/status":

            self.send({

            "dashboard":dashboard(),

            "workspace":scan(),

            "engine":"XDEPLOY v13"

            })


        elif self.path=="/deploy":

            r=deploy()

            emit(
            "DEPLOY_TRIGGER",
            r
            )

            self.send(r)



        elif self.path=="/rollback":

            r=rollback()

            emit(
            "ROLLBACK_TRIGGER",
            r
            )

            self.send(r)



        elif self.path=="/events":

            self.send(
            history()
            )


        else:

            self.send(
            {
            "error":"NOT_FOUND"
            }
            )



def start():

    print(
"""
╔════════════════════════════╗
║ XDEPLOY v13 WEB ONLINE    ║
║ http://127.0.0.1:8088     ║
╚════════════════════════════╝
"""
)


    HTTPServer(
    ("0.0.0.0",8088),
    Handler

    ).serve_forever()



if __name__=="__main__":

    start()

PY



echo "[3] Creating launcher"


cat > xdeploy_web.py <<'PY'
from Core.dashboard.web.server import start

start()
PY



echo "[4] Testing"


python - <<'PY'

from Core.dashboard.web.server import HTML

print(
"WEB MODULE READY"
)

PY



echo "
╔══════════════════════════════════════╗
║        XDEPLOY v13 COMPLETE           ║
╚══════════════════════════════════════╝


RUN:

python xdeploy_web.py


OPEN:

http://127.0.0.1:8088

"

