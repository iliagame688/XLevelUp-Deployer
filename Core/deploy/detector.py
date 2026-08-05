from pathlib import Path


class PlatformDetector:


    def detect(self, path):

        root = Path(path)


        files = [
            x.name
            for x in root.iterdir()
            if x.is_file()
        ] if root.exists() else []


        result = {
            "platform": "UNKNOWN",
            "files": files
        }


        if "railway.json" in files:

            result["platform"] = "RAILWAY"


        elif "vercel.json" in files:

            result["platform"] = "VERCEL"


        elif "Dockerfile" in files:

            result["platform"] = "DOCKER"


        elif "docker-compose.yml" in files:

            result["platform"] = "DOCKER_COMPOSE"


        elif "requirements.txt" in files:

            result["platform"] = "PYTHON_SERVICE"


        return result



detector = PlatformDetector()
