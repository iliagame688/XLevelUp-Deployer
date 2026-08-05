from collections import Counter


class StructureAnalyzer:


    def analyze(self, files):


        names = [

            item["name"]

            for item in files

        ]


        duplicates = [

            name

            for name,count in Counter(names).items()

            if count > 1

        ]


        large = [

            item["path"]

            for item in files

            if item["size"] > 500000

        ]


        return {


            "total_files":

                len(files),


            "duplicates":

                duplicates,


            "large_files":

                large

        }




analyzer = StructureAnalyzer()
