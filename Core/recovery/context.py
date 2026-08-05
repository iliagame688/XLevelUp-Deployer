import linecache


def error_context(file_path, line, radius=5):

    start=max(1,line-radius)
    end=line+radius

    data=[]

    for i in range(start,end+1):

        text=linecache.getline(
            file_path,
            i
        )

        if text:

            data.append(
                {
                "line":i,
                "code":text.rstrip()
                }
            )

    return data


