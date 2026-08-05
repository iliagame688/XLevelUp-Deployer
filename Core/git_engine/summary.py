class ChangeSummary:


    def build(self, changes):


        added = len(
            changes.get(
                "added",
                []
            )
        )


        modified = len(
            changes.get(
                "modified",
                []
            )
        )


        removed = len(
            changes.get(
                "removed",
                []
            )
        )


        return {

            "added":
                added,

            "modified":
                modified,

            "removed":
                removed

        }



summary = ChangeSummary()
