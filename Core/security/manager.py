from pathlib import Path
import json


VAULT = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/security/.vault.json"
)



def save_secret(
    name,
    value
):

    data = {}


    if VAULT.exists():

        try:

            data = json.loads(
                VAULT.read_text(
                    encoding="utf-8"
                )
            )

        except:

            data = {}


    data[name] = value


    VAULT.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    VAULT.write_text(
        json.dumps(
            data,
            indent=4
        ),
        encoding="utf-8"
    )



def get_secret(
    name
):

    if not VAULT.exists():

        return None


    try:

        data = json.loads(
            VAULT.read_text(
                encoding="utf-8"
            )
        )

        return data.get(
            name
        )

    except:

        return None
