from Core.live.session import session


class LiveLogger:



    def event(
        self,
        operation,
        status,
        detail=""
    ):

        return session.add(
            operation,
            status,
            detail
        )




logger = LiveLogger()
