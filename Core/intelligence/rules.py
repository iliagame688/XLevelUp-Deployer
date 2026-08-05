RULES = {

    "ModuleNotFoundError": {

        "type":
            "IMPORT_ERROR",

        "cause":
            "Module path or package structure problem",

        "suggestion":
            "Check Core imports and package layout",

        "confidence":
            94

    },


    "FileNotFoundError": {

        "type":
            "MISSING_FILE",

        "cause":
            "Required file does not exist",

        "suggestion":
            "Create file or repair configuration",

        "confidence":
            91

    },


    "PermissionError": {

        "type":
            "PERMISSION_ERROR",

        "cause":
            "Access permission denied",

        "suggestion":
            "Check storage or execution permissions",

        "confidence":
            88

    }

}
