
import hashlib


class Security:


    def mask(self, value):

        if not value:
            return ""


        if len(value) <= 6:
            return "***"


        return (

            value[:3]

            +

            "***"

            +

            value[-3:]

        )


    def fingerprint(self, value):

        return hashlib.sha256(

            value.encode()

        ).hexdigest()[:12]




security = Security()

