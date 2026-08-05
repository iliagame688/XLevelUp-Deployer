from Core.dashboard.layout.device import detect



class LayoutManager:


    def current(self):

        return detect()



    def panels(self):

        mode = self.current()


        if mode == "COMPACT":

            return [

                "STATUS",

                "LIVE"

            ]


        elif mode == "MOBILE":

            return [

                "STATUS",

                "ENGINE",

                "LIVE"

            ]


        return [

            "STATUS",

            "ENGINE",

            "PIPELINE",

            "LIVE"

        ]



layout = LayoutManager()

