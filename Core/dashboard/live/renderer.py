
class LiveRenderer:


    def show(self, events):


        print("""
╭──────── XDEPLOY LIVE ────────╮
""")


        for event in events:


            percent = event.get(
                "progress"
            )


            if percent is not None:


                size = 25


                filled = int(
                    size * percent / 100
                )


                bar = (

                    "█" * filled

                    +

                    "░" * (size-filled)

                )


                print(

                    f"{event['message']:<20}"

                    f"[{bar}] {percent}%"

                )


            else:


                print(

                    f"{event['level']}: "

                    f"{event['message']}"

                )



        print("""
╰─────────────────────────────╯
""")



renderer = LiveRenderer()

