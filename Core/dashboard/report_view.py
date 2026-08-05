

class ReportView:


    def show(self, report):


        print(
"""
╭──────── RESULT ────────╮
"""
        )


        print(
            "Status:",
            report.get("status")
        )


        print(
            "Steps:"
        )


        for step in report.get(
            "steps",
            []
        ):

            print(
                " ✓",
                step
            )


        print(
"""
╰────────────────────────╯
"""
        )




report_view = ReportView()

