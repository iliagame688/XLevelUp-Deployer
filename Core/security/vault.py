from pathlib import Path


VAULT = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/security/.vault"
)



def save(key, value):

    VAULT.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    VAULT.write_text(
        f"{key}:{value}",
        encoding="utf-8"
    )



def exists():

    return VAULT.exists()
