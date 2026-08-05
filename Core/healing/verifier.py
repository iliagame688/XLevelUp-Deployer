
def verify(action):


    # اینجا بعداً تست واقعی Engine قرار می‌گیرد


    if action:

        return {

            "verified":
                True,

            "status":
                "FIXED"

        }



    return {

        "verified":
            False,

        "status":
            "FAILED"

    }

