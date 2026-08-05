from rich.table import Table


def engine_table(data):


    table = Table(
        title="ENGINE STATUS"
    )


    table.add_column(
        "ENGINE"
    )


    table.add_column(
        "STATUS"
    )


    for name,item in data.items():


        status = item.get(
            "status",
            "UNKNOWN"
        )


        icon = "🟢"


        if status == "RUNNING":

            icon = "🟡"


        elif status == "FAILED":

            icon = "🔴"



        table.add_row(

            name,

            f"{icon} {status}"

        )


    return table

