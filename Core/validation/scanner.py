from Core.validation.tester import tester



class SystemScanner:


    def scan(self, modules):


        results = []


        for module in modules:


            results.append(

                tester.test(
                    module
                )

            )


        return results




scanner = SystemScanner()
