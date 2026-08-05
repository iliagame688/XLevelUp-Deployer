
import time
import sys


class ProgressManager:


    def bar(self, name, percent):

        size = 30

        filled = int(
            size * percent / 100
        )


        bar = (
            "█" * filled
            +
            "░" * (size-filled)
        )


        sys.stdout.write(

            f"\r{name:<20} [{bar}] {percent}%"

        )


        sys.stdout.flush()



    def run(self, name):


        for i in range(
            0,
            101,
            10
        ):

            self.bar(
                name,
                i
            )

            time.sleep(
                0.05
            )


        print()



progress = ProgressManager()

