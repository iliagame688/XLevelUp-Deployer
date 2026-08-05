from pathlib import Path


ROOT = Path("/storage/emulated/0/XLevelUp-Deployer")
CORE = ROOT / "Core"


def health_check():

    checks = {
        "Root": ROOT.exists(),
        "Core": CORE.exists(),
        "Engine": (CORE/"engine").exists(),
        "Config": (CORE/"config").exists(),
        "Data": (CORE/"data").exists()
    }

    return checks


if __name__ == "__main__":

    print("XDEPLOY HEALTH CHECK")

    for name, result in health_check().items():
        print(
            f"{name}:",
            "✓" if result else "✗"
        )
