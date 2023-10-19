import reflex as rx



def navbar():
    navbar = rx.flex(
        rx.box(
            rx.link(
                rx.image(src = "/WebscraperBusinessLogo.jpeg", width = '45px'),
                href = "/")
        ),
        rx.center(
            rx.menu(
                rx.menu_button('MENU', color = 'white'),
                rx.menu_list(
                    rx.menu_item(
                        rx.link("Home", href="/")
                    ),
                    rx.menu_item(
                        rx.link("Add Product", href="/addproduct")
                    ),
                    rx.menu_item(
                        rx.link("Remove Product", href = "/removeproduct")
                    )
                )
            ),
            margin_x = '1rem'
        ),
        width = '100%',
        justify_content = 'space-between'
    )

    return navbar