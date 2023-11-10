import reflex as rx
import os
from dotenv import load_dotenv
from .components.navbar import navbar
from .components.productinputbox import product_input_box, InputState
from .components.productlist import productlist, SelectState



load_dotenv()

ORGANIZATION_NAME = os.getenv("ORGANIZATION_NAME")



#creating main page
def index():
    return rx.box(
        rx.responsive_grid(
            navbar(),
            rx.center(
                rx.text(
                    f"Welcome, {ORGANIZATION_NAME}",
                    font_size = '85px',
                    as_ = "b",
                    background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                    background_clip="text",
                    margin_top = '2rem'
                ),
                center_content = True,
                margin_top = "15rem"
            ),

            rows = [2]
        ),
        width = '100%',
        height = '100%',
        position = 'fixed',
        top = '0px',
        left = '0px',
        background_color = '#fafafa'
    )




#creating page to add product
def add_product_page():
    return rx.box(
        rx.responsive_grid(
            navbar(),
            rx.divider(),
            rx.center(
                rx.text(
                    "Add Product",
                    font_size = '50px',
                    margin_top = '2rem',
                 )
            ),
            product_input_box(),
            rx.box(
                rx.button(
                    InputState.text,
                    text_color = "#fafafa",
                    bg = "#fafafa",
                    _hover = {"bg": "#fafafa"}
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
        background_color = '#fafafa',
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
        background_color = "#fafafa"
    )



def scrape_table_page():
    return rx.box(
        rx.responsive_grid(
            navbar(),
            rx.divider(),
            rx.center(
                rx.text(
                    "Scrape Table",
                    font_size = "50px",
                    margin_top = "2rem"
                )
            ),
            rx.box(
                productlist(show_scrapes_button = True),
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
        background_color = "#fafafa",
        overflow = "auto"
    )



#changing text color in certain areas to improve visibility
"""
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
""" #temp



#compiling app
app = rx.App()
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
app.add_page(
    scrape_table_page,
    route = "/scrapetable",
    title = "Web-Scraper",
    image = "/favicon.ico"
)
app.compile()