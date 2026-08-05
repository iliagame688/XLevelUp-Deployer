from pathlib import Path


ROOT = Path(
    "/storage/emulated/0/XLevelUp-Deployer"
)



def check():


    result = {

        "core":
            (ROOT / "Core").exists(),

        "engine":
            (ROOT / "Core/engine").exists(),

        "deploy":
            (ROOT / "Core/deploy").exists(),

        "dashboard":
            (ROOT / "Core/dashboard").exists(),

    }


    result["health"] = (
        "GOOD"
        if all(result.values())
        else
        "WARNING"
    )


    return result



if __name__ == "__main__":

    print(check())
