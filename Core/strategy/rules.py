
DEPLOY_RULES = {


    "PYTHON":
    {

        "flow":
            "PYTHON_PIPELINE",

        "steps":
        [

            "CHECK_REQUIREMENTS",

            "INSTALL_DEPENDENCIES",

            "BUILD",

            "DEPLOY",

            "VERIFY"

        ]

    },


    "NODE":
    {

        "flow":
            "NODE_PIPELINE",

        "steps":
        [

            "CHECK_PACKAGE",

            "NPM_INSTALL",

            "BUILD",

            "DEPLOY",

            "VERIFY"

        ]

    },


    "DOCKER":
    {

        "flow":
            "CONTAINER_PIPELINE",

        "steps":
        [

            "CHECK_DOCKERFILE",

            "BUILD_IMAGE",

            "START_CONTAINER",

            "VERIFY"

        ]

    },


    "UNKNOWN":
    {

        "flow":
            "GENERIC_PIPELINE",

        "steps":
        [

            "SCAN",

            "PREPARE",

            "DEPLOY"

        ]

    }

}

