#!/data/data/com.termux/files/usr/bin/bash

PROJECT="/storage/emulated/0/XLevelUp-Deployer"

cd "$PROJECT"


python - <<'PY'

from pathlib import Path


p=Path("Core/control/menu.py")

text=p.read_text()


text=text.replace(
'print(\\n            deploy()\\n            )',
'print(deploy())\\n            input("\\nPress ENTER to continue...")'
)


text=text.replace(
'print(\\n            scan()\\n            )',
'print(scan())\\n            input("\\nPress ENTER to continue...")'
)


text=text.replace(
'print(\\n            create()\\n            )',
'print(create())\\n            input("\\nPress ENTER to continue...")'
)


text=text.replace(
'else:\\n\\n            print(\\n            "INVALID COMMAND"\\n            )',
'else:\\n\\n            print("INVALID COMMAND")\\n            input("\\nPress ENTER...")'
)


p.write_text(text)

PY


python -m py_compile Core/control/menu.py


echo "
╔════════════════════════════════╗
║ XDEPLOY v26.1 PATCH COMPLETE   ║
╚════════════════════════════════╝
"

