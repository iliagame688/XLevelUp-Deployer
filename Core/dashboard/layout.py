from rich.layout import Layout


def create():

    root = Layout()


    root.split_column(

        Layout(
            name="header",
            size=3
        ),

        Layout(
            name="body"
        )

    )


    root["body"].split_row(

        Layout(
            name="left"
        ),

        Layout(
            name="right"
        )

    )


    return root
