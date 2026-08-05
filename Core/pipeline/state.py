
class PipelineState:


    def __init__(self):

        self.steps = []


    def add(self, step):

        self.steps.append(step)


    def get(self):

        return self.steps



state = PipelineState()

