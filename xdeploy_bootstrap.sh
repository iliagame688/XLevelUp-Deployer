#!/data/data/com.termux/files/usr/bin/bash

set -e

PROJECT="/storage/emulated/0/XLevelUp-Deployer"
SECURITY_DIR="$PROJECT/Core/security"
AUTH_FILE="$SECURITY_DIR/github_auth.json"

REPO="https://github.com/iliagame688/XLevelUp-Deployer.git"

echo "
╔══════════════════════════════════════╗
║     XLEVELUP DEPLOYER BOOTSTRAP     ║
║          REAL DEPLOY ENGINE          ║
╚══════════════════════════════════════╝
"


cd "$PROJECT"


echo "[1] Checking environment..."

command -v git >/dev/null || {
    echo "Git missing"
    pkg install git -y
}


echo "[2] Git identity check..."

git config user.name >/dev/null || \
git config user.name "iliagame688"


git config user.email >/dev/null || \
git config user.email "iliagame688@users.noreply.github.com"



echo "[3] Security protection..."

cat > .gitignore <<'EOF'
# Secrets
.env
*.token
*.secret

Core/security/github_token.json
Core/security/github_auth.json
Core/security/.vault.json

vault.json

# Credentials
Core/data/credentials.json
Core/data/real_vault.json

# Python
__pycache__/
*.pyc

# Logs
*.log
EOF



echo "[4] Removing exposed secrets from staging..."

rm -f Core/security/github_token.json 2>/dev/null || true



echo "[5] Token manager..."

mkdir -p "$SECURITY_DIR"


if [ ! -f "$AUTH_FILE" ]; then

echo "
╔══════════════════════════════╗
║ GitHub Token Required         ║
╚══════════════════════════════╝
"

read -s -p "Input Token: " TOKEN

echo


if [ -z "$TOKEN" ]; then
    echo "TOKEN EMPTY"
    exit 1
fi


cat > "$AUTH_FILE" <<EOF
{
    "provider":"github",
    "username":"iliagame688",
    "token":"$TOKEN"
}
EOF


chmod 600 "$AUTH_FILE"


echo "✓ TOKEN SAVED"

else

echo "✓ TOKEN EXISTS"

fi



echo "[6] Git repository..."

if [ ! -d ".git" ]; then

    git init

fi


git branch -M main



echo "[7] Remote setup..."

if git remote | grep -q origin; then

    git remote set-url origin "$REPO"

else

    git remote add origin "$REPO"

fi



echo "[8] Secret scan..."

FOUND=$(grep -RIl \
-E "(ghp_|github_pat_|AKIA|BEGIN PRIVATE KEY|token)" \
. \
--exclude-dir=.git \
--exclude="xdeploy_bootstrap.sh" \
2>/dev/null || true)



if [ ! -z "$FOUND" ]; then

echo "
⚠ POSSIBLE SECRETS FOUND:
"

echo "$FOUND"


echo "
Removing from git index...
"


for f in $FOUND
do
git rm --cached "$f" 2>/dev/null || true
done


fi



echo "[9] Commit..."

git add .

git commit \
-m "XLEVELUP SAFE DEPLOY $(date)" \
|| echo "Nothing new"



echo "[10] Push..."

set +e

git push \
--set-upstream \
origin main


RESULT=$?


set -e



echo "
╔══════════════════════════════════════╗
║          XDEPLOY REPORT              ║
╚══════════════════════════════════════╝
"


if [ $RESULT -eq 0 ]; then

echo "
STATUS: SUCCESS

✓ Repository Connected
✓ Commit Created
✓ Push Completed
✓ Security Layer Active

NEXT:
- Enable Auto Deploy Engine
- Enable Workspace Watcher
- Enable AI Recovery
"

else

echo "
STATUS: PUSH FAILED

Possible reasons:

1. GitHub Token invalid
2. Remote contains newer commits
3. Branch protection enabled
4. Token permission missing

NEXT COMMAND:

git pull origin main --rebase

then:

git push
"

fi


echo "
XLEVELUP BOOTSTRAP COMPLETE
"

