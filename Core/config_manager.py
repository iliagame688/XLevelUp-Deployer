
class ConfigManager:

    def __init__(self):
        self.data = {
            "mode": "REAL",
            "deploy": True,
            "test": False
        }


    def get(self,key,default=None):
        return self.data.get(
            key,
            default
        )


    def load(self):
        return self.data



config_manager = ConfigManager()
