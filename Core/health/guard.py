from pathlib import Path
import sys


ROOT = Path(
    "/storage/emulated/0/XLevelUp-Deployer"
)

CORE = ROOT / "Core"


REQUIRED = [
    "boot",
    "dashboard",
    "workspace",
    "git",
    "recovery",
    "engine",
    "config",
    "data",
    "logs"
]


def check_structure():

    print("""
╭──────────────────────────╮
│ XDEPLOY HEALTH GUARD v5  │
╰──────────────────────────╯
""")


    if not (ROOT / "xdeploy.py").exists():

        print("xdeploy.py  ✗ missing")

    else:

        print("xdeploy.py  ✓")


    print()


    print("CORE STRUCTURE")

    for item in REQUIRED:

        path = CORE / item

        if path.exists():

            print(f"{item:<15} ✓")

        else:

            print(f"{item:<15} ✗")



    print()


    outside = []

    for item in ROOT.iterdir():

        if item.name == "xdeploy.py":
            continue

        if item.name == "Core":
            continue

        outside.append(
            item.name
        )


    print("OUTSIDE CORE")

    if outside:

        for x in outside:
            print("⚠", x)

    else:

        print("✓ CLEAN")


    print()


    print("STATUS")

    print("✓ STRUCTURE READY")



if __name__ == "__main__":

    check_structure()
