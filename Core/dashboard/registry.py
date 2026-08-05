class PanelRegistry:

    def __init__(self):
        self.panels = {}

    def register(self, name, panel):
        self.panels[name] = panel

    def get(self, name):
        return self.panels.get(name)

    def all(self):
        return self.panels


registry = PanelRegistry()
