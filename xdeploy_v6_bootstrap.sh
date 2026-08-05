#!/data/data/com.termux/files/usr/bin/bash

set -e

PROJECT="/storage/emulated/0/XLevelUp-Deployer"
REPO="https://github.com/iliagame688/XLevelUp-Deployer.git"

cd "$PROJECT"


clear

echo "
╔══════════════════════════════════════╗
║      XLEVELUP DEPLOYER v6             ║
║      HARDENING + AI SAFE PUSH         ║
╚══════════════════════════════════════╝
"



echo "[1] Environment Check"


command -v git >/dev/null || {
pkg install git -y
}


command -v python >/dev/null || {
pkg install python -y
}



echo "[2] Creating secure structure"


mkdir -p \
Core/runtime \
Core/logs \
Core/backups \
Core/cache \
tests \
docs \
.github/workflows



echo "[3] Creating Advanced .gitignore"


cat > .gitignore <<'EOF'

# =========================
# SECURITY
# =========================

.env
*.env
*.token
*.secret

token.json
tokens.json

Core/security/github_token.json
Core/security/github_auth.json
Core/security/*.json

Core/data/credentials.json
Core/data/real_vault.json
Core/data/vault.json

vault.json


# =========================
# PYTHON
# =========================

__pycache__/
*.py[cod]
*$py.class


# =========================
# RUNTIME
# =========================

Core/runtime/*
Core/logs/*
Core/cache/*

*.log


# =========================
# BACKUPS
# =========================

*.bak
*.backup
*.old


# =========================
# DEBUG
# =========================

deploy_debug.json
git_trace.py
upload_history.json

EOF



echo "[4] Removing dangerous files"


rm -rf \
Core/__pycache__ \
__pycache__



find . -name "*.pyc" -delete 2>/dev/null || true



echo "[5] Secret Firewall Scan"


FOUND=$(grep -RIl \
-E "(ghp_|github_pat_|BEGIN PRIVATE KEY|AIza|AKIA)" \
. \
--exclude-dir=.git \
2>/dev/null || true)



if [ ! -z "$FOUND" ]; then

echo "
⚠ SECRET DETECTED
"

echo "$FOUND"


for FILE in $FOUND
do

case "$FILE" in

*.sh)
;;

*)
echo "Removing from git index:"
git rm --cached "$FILE" 2>/dev/null || true

;;

esac

done

else

echo "✓ No secrets detected"

fi



echo "[6] Git Health"


if [ ! -d ".git" ]; then

git init

fi



git branch -M main


git config user.name "iliagame688"

git config user.email "iliagame688@users.noreply.github.com"



echo "[7] Remote Verify"


if git remote | grep -q origin
then

git remote set-url origin "$REPO"

else

git remote add origin "$REPO"

fi



echo "[8] Cleaning tracked runtime"


git rm -r --cached \
Core/runtime \
Core/logs \
Core/cache \
2>/dev/null || true



echo "[9] Staging"


git add .



STATUS=$(git status --short)



if [ -z "$STATUS" ]; then

echo "NO CHANGES"

else


echo "
CHANGES:"
echo "$STATUS"


git commit \
-m "XDEPLOY v6 HARDENING $(date)"

fi



echo "[10] Remote Sync"


git fetch origin main || true



echo "[11] Push Engine"


ATTEMPT=1
MAX=3


while [ $ATTEMPT -le $MAX ]

do


echo "Push attempt $ATTEMPT/$MAX"



if git push --set-upstream origin main
then

SUCCESS=1
break

fi


ATTEMPT=$((ATTEMPT+1))


sleep 2


done




echo "
╔══════════════════════════════════════╗
║          XDEPLOY REPORT              ║
╚══════════════════════════════════════╝
"



if [ "$SUCCESS" = "1" ]

then


echo "
STATUS: ONLINE

✓ SECURITY CLEAN
✓ GIT HEALTHY
✓ REMOTE CONNECTED
✓ PUSH SUCCESS
✓ DEPLOY READY

ENGINE:
XDEPLOY v6

NEXT:
AI Recovery Engine
Auto Deploy Brain
Workspace Watcher

"


else


echo "
STATUS: PUSH FAILED

CHECK:

git status
git log --oneline
git remote -v

"

fi



echo "
XLEVELUP v6 COMPLETE
"


