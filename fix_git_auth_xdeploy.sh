#!/data/data/com.termux/files/usr/bin/bash

set -e


echo "
╔════════════════════════════════╗
║ XDEPLOY GIT AUTH FIX           ║
╚════════════════════════════════╝
"


mkdir -p Core/security


if [ ! -f Core/security/github_auth.json ]; then

echo "GitHub Token Required"

read -s -p "Enter GitHub PAT: " TOKEN

echo


cat > Core/security/github_auth.json <<EOF
{
 "provider":"github",
 "username":"iliagame688",
 "token":"$TOKEN"
}
EOF


chmod 600 Core/security/github_auth.json

else

echo "Existing Auth Found"

fi



python - <<'PY'

import json

with open(
"Core/security/github_auth.json"
) as f:

    data=json.load(f)


print({

"user":data.get("username"),

"token":"LOADED"

})

PY



echo "
AUTH READY

Next:
git push origin main
"

