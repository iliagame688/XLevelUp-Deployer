
class PluginManager:


    def __init__(self):

        self.plugins = {}



    def install(
        self,
        name,
        module
    ):

        self.plugins[name] = {

            "module":
                module,

            "status":
                "ACTIVE"

        }


        return self.plugins[name]




    def remove(
        self,
        name
    ):

        if name in self.plugins:

            del self.plugins[name]


        return True




    def list(self):

        return self.plugins




plugins = PluginManager()

