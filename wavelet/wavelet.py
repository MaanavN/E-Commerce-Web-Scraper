import reflex as rx
from .components.navbar import navbar
from .components.productinputbox import product_input_box, InputState
from .components.productlist import productlist, SelectState



#creating main page
def index():
    return rx.box(
        rx.responsive_grid(
            navbar(),
            rx.divider(),
            rx.center(
                rx.text(
                    "Web-Scraper",
                    font_size = '85px',
                    color = "white",
                    margin_top = '2rem',
                ),
            ),
            rx.center(
                rx.text(
                    "Interface",
                    font_size = '85px',
                    color = 'white',
                ),
            ),
            rx.box(
                productlist(show_scrapes_button = True),
                margin_top = "1.5rem"
            ),

            rows = [5]
        ),
        width = '100%',
        height = '100%',
        position = 'fixed',
        top = '0px',
        left = '0px',
        background_color = 'rgb(45,47,59)'
    )


#changing text color in certain areas to improve visibility
style = {
        rx.Input: {
            "color": "rgb(188,188,188)"
        },
        rx.Checkbox: {
            "color": "rgb(188,188,188)"
        },
        rx.Select: {
            "color": "rgb(188,188,188)"
        }
    }

#creating page to add product
def add_product_page():
    return rx.box(
        rx.responsive_grid(
            navbar(),
            rx.divider(),
            rx.center(
                rx.text(
                    "Add Product",
                    color = "white",
                    font_size = '50px',
                    margin_top = '2rem',
                 )
            ),
            product_input_box(),
            rx.box(
                rx.button(
                    InputState.text,
                    text_color = "rgb(45,47,59)",
                    bg = "rgb(45,47,59)",
                    _hover = {"bg": "rgb(45,47,59)"}
                ),
                width = "20px"
            ),

            rows = [5]
        ),

        width = '100%',
        height = '100%',
        position = 'fixed',
        top = '0px',
        left = '0px',
        background_color = 'rgb(45,47,59)',
    )



#creating page to remove product
def remove_product_page():
    return rx.box(
        rx.responsive_grid(
            navbar(),
            rx.divider(),
            rx.center(
                rx.text(
                    "Remove Product",
                    color = "white",
                    font_size = "50px",
                    margin_top = "2rem"
                )
            ),
            rx.box(
                productlist(remove_product_button = True),
                margin_top = "2rem",
                text_align = "center"
            ),

            rows = [4]
        ),

        width = "100%",
        height = "100%",
        position = "fixed",
        top = "0px",
        left = "0px",
        background_color = "rgb(45,47,59)"
    )



#compiling app
app = rx.App(style = style)
app.add_page(index, image = "/favicon.ico", title = "Web-Scraper")
app.add_page(
    add_product_page,
    route = '/addproduct',
    title = "Web-Scraper",
    image = "/favicon.ico",
    on_load = InputState.reset_self()
    )
app.add_page(
    remove_product_page,
    route = "/removeproduct",
    title = "Web-Scraper",
    image = "/favicon.ico",
    on_load = SelectState.reset_self()
)
app.compile()