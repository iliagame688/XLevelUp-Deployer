
def show(result):

    print()

    print(
    "╭──────── XLEVELUP REAL DEPLOY ────────╮"
    )


    print()

    print(
        "ENGINE:",
        result.get(
            "engine",
            "REAL"
        )
    )


    print(
        "STATUS:",
        result.get(
            "status"
        )
    )


    print()


    for step in result.get(
        "steps",
        []
    ):

        print(
            "✓",
            step.get(
                "name"
            )
        )


    print()

    print(
    "╰──────────────────────────────────────╯"
    )

