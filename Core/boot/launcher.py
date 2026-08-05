from Core.integrity.checker import checker


class BootManager:



    def start(self):


        print(

            "\n╭──── XCONTROL BOOT ────╮"

        )


        print(
            "Checking Core..."
        )


        result = checker.run()


        failed = [

            x for x in result["modules"]

            if x["status"] == "ERROR"

        ]



        if failed:


            print(
                "\n🔴 CORE ERROR DETECTED"
            )


            for item in failed:

                print(
                    item["module"],
                    item["error"]
                )


            return False



        print(
            "🟢 Core Integrity OK"
        )


        print(
            "🟢 Engines Loaded"
        )


        return True





boot = BootManager()
