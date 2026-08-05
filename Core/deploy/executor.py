import json
from pathlib import Path


from Core.deploy.task import create
from Core.engine.hub import engine



QUEUE = Path(
    "/storage/emulated/0/XLevelUp-Deployer/Core/data/deploy_queue.json"
)



def load():

    if not QUEUE.exists():

        return []

    try:

        return json.loads(
            QUEUE.read_text(
                encoding="utf-8"
            )
        )

    except:

        return []




def save(data):

    QUEUE.write_text(

        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ),

        encoding="utf-8"

    )




def execute():

    tasks = load()


    results = []


    for task in tasks:


        if task["status"] == "WAITING":


            task["status"] = "RUNNING"


            # فعلاً شبیه سازی Provider
            # مرحله بعد Provider واقعی اضافه می‌شود


            task["status"] = "SUCCESS"


        results.append(task)



    save(tasks)


    engine.update(
        "DEPLOY",
        "EXECUTED"
    )


    engine.snapshot()


    return results




if __name__ == "__main__":

    print(execute())
