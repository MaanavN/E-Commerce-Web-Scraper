import reflex as rx



def navbar():
    navbar = rx.flex(
        rx.box(
            rx.responsive_grid(
                rx.center(
                    rx.link(
                        rx.text(
                            "Wavelet",
                            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                            background_clip="text",
                            font_weight="bold",
                            font_size="2em",
                        ),
                        href = "/"
                    ),
                    margin_left = "3rem"
                ),
                rx.center(
                    rx.link(
                        rx.text(
                            "Add Product",
                            font_size = "1rem",
                            as_ = "b"
                        ),
                        href = "/addproduct"
                    ),
                    margin_left = "3rem"
                ),
                rx.center(
                    rx.link(
                        rx.text(
                            "Remove Product",
                            font_size = "1rem",
                            as_ = "b"
                        ),
                        href = "/removeproduct"
                    ),
                    margin_left = "2rem"
                ),
                rx.center(
                    rx.link(
                        rx.text(
                            "Scrape Table",
                            font_size = "1rem",
                            as_ = "b"
                        ),
                        href = "/scrapetable"
                    ),
                    margin_left = "2rem"
                ),
                columns = [4]
            )
        ),
        width = '100%',
        justify_content = 'space-between',
        shadow = "md"
    )

    return navbar