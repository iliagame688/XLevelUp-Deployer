#!/usr/bin/env python3

from Core.dashboard import dashboard
from Core.watcher.intelligence import scan
from Core.deploy.agent import run


def main():

    print("""
╔══════════════════════════════════╗
║       XLEVELUP LIVE CENTER       ║
║          XDEPLOY v10              ║
╚══════════════════════════════════╝
""")


    print("\n[DASHBOARD]")
    print(
        dashboard()
    )


    print("\n[WORKSPACE]")
    print(
        scan()
    )


    print("\n[DEPLOY ENGINE]")
    print(
        run()
    )


if __name__=="__main__":
    main()

