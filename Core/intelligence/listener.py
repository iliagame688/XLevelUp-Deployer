from Core.intelligence.events import push
from Core.intelligence.analyzer import analyze



class IntelligenceListener:


    def __init__(self):

        self.name = "INTELLIGENCE"


    def error(
        self,
        module,
        error
    ):

        result = analyze(
            module,
            error
        )


        push(
            module,
            "ERROR_ANALYZED",
            result
        )


        return result



    def event(
        self,
        source,
        name,
        data=None
    ):

        return push(
            source,
            name,
            data
        )



listener = IntelligenceListener()
