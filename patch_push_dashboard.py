import os


targets=[]

for root,dirs,files in os.walk("Core/dashboard"):
    for f in files:
        if f.endswith(".py"):
            path=os.path.join(root,f)

            try:
                data=open(path).read()

                if 'data["push"]' in data:
                    targets.append(path)

            except:
                pass


if not targets:
    print("NO DASHBOARD TARGET FOUND")
    exit()


for file in targets:

    data=open(file).read()


    old='push = data["push"]'


    new='''from Core.git.push_status import format_push_status

push = format_push_status(
    data.get("push", {})
)'''


    if old in data:

        data=data.replace(
            old,
            new
        )

        open(file,"w").write(data)

        print(
            "PATCHED:",
            file
        )

    else:
        print(
            "SKIP:",
            file
        )


