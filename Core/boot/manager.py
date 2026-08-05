from Core.boot.stages import stages



class BootManager:


    def start(self):


        result = stages.run()


        print(

            "\n╭──────────────────╮"

        )

        print(

            " XLEVELUP BOOT "

        )

        print(

            "╰──────────────────╯\n"

        )


        for item in result:


            print(

                "✓",

                item["name"],

                item["state"]

            )


        print(

            "\nENGINE ONLINE"

        )


        return True





boot = BootManager()
