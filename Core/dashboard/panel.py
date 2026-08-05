
class StatusPanel:


    def render(self, data):

        print(
"\n╭──────── STATUS ────────╮"
        )


        for key,value in data.items():

            print(
                f"│ {key:<12}: {value}"
            )


        print(
"╰────────────────────────╯"
        )




panel = StatusPanel()

