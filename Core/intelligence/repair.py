def repair(error_type):


    fixes = {

        "AUTO_DEPENDENCY":
            "Install missing dependency",

        "AUTO_FILE_FIX":
            "Restore missing file",

        "AUTO_IMPORT_FIX":
            "Repair import structure"

    }


    return fixes.get(

        error_type,

        "Manual action required"

    )
