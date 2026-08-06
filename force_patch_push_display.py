import os


for root,dirs,files in os.walk("Core"):

    for f in files:

        if not f.endswith(".py"):
            continue

        path=os.path.join(root,f)

        try:
            data=open(path).read()

        except:
            continue


        if (
            "last_deploy" in data
            or
            "PUSH:" in data
            or
            '["push"]' in data
        ):

            print("FOUND:",path)


            data=data.replace(
                'data["push"]',
                'format_push_status(data.get("push", {}))'
            )


            if "format_push_status" not in data:

                data=(
                    "from Core.git.push_status import format_push_status\n"
                    + data
                )


            open(path,"w").write(data)


print("XDEPLOY PUSH DISPLAY PATCH COMPLETE")

