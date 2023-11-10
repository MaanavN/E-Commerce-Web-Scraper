import reflex as rx
import models
from icecream import ic
from .BaseState import BaseState



# This function gets a list of products from the database

def get_product_list():
    product_list = []
    
    try:
        with open("product_names.txt", "r") as file:
            lines = file.readlines()
            product_list = [line.strip() for line in lines]
    except FileNotFoundError:
        pass

    return product_list


# Creating State
class SelectState(BaseState):
    selection: str = ""
    product_list = get_product_list()
    display_scrape_data = False
    product: dict

    # Refreshes the list of products
    def refresh_list(self):
        self.product_list = get_product_list()

    # Removes the selected product from the database
    def remove_product(self):
        models.delete_product(self.selection) # Delete selected product

    def show_scrapes(self):
        if self.selection != "":
            self.display_scrape_data = not self.display_scrape_data

            if self.display_scrape_data == True:
                product = models.query_database(self.selection)
                self.product = product

                ic(f"Product: {self.product}") #temp


    # Resets State
    def reset_self(self):
        self.reset() # Reset state


# Return the select component with the given options
def productlist(remove_product_button=False, show_scrapes_button=False):
    if remove_product_button == False and show_scrapes_button == False:
        return rx.responsive_grid(
            rx.container(
                rx.select(
                    SelectState.product_list, # List of products to display
                    placeholder="Select Product", # Placeholder text
                    on_change=SelectState.set_selection # Function to call when selection changes
                )
            ),
            rx.center(
                rx.hstack(
                    rx.button(
                        "Refresh List",
                        on_click=SelectState.refresh_list() # Function to call when button is clicked
                    ),
                    margin_top = "1rem"
                )
            ),

            rows = [2]
        )
    elif remove_product_button == True:
        return rx.responsive_grid(
            rx.container(
                rx.select(
                    SelectState.product_list, # List of products to display
                    placeholder="Select Product", # Placeholder text
                    on_change=SelectState.set_selection # Function to call when selection changes
                )
            ),
            rx.center(
                rx.hstack(
                    rx.button(
                        "Refresh List",
                        on_click=SelectState.refresh_list() # Function to call when button is clicked
                    ),
                    rx.button(
                        "Remove Product", # Button text
                        on_click=SelectState.remove_product() # Function to call when button is clicked
                    ),
                    margin_top = "1rem"
                )
            ),

            rows = [2]
        )
    elif show_scrapes_button == True:
        return rx.responsive_grid(
            rx.container(
                rx.select(
                    SelectState.product_list, # List of products to display
                    placeholder="Select Product", # Placeholder text
                    on_change=SelectState.set_selection # Function to call when selection changes
                )
            ),
            rx.center(
                rx.hstack(
                    rx.button(
                        "Refresh List",
                        on_click=SelectState.refresh_list() # Function to call when button is clicked
                    ),
                    rx.button(
                        "Show Scrapes", # Button text
                        on_click=SelectState.show_scrapes() # Function to call when button is clicked
                    ),
                    margin_top = "1rem"
                )
            ),
            rx.cond(
                SelectState.display_scrape_data,
                rx.responsive_grid(
                    rx.box(
                        rx.text(
                            SelectState.product["product_name"]
                        ),
                        margin_bottom = "2rem"
                    ),
                    rx.box(
                        rx.text(
                            SelectState.product["sites"]
                        ),
                        margin_bottom = "2rem"
                    ),
                    rx.box(
                        rx.text(
                            SelectState.product["results"]
                        ),
                        margin_x = "5rem"
                    ),
                    margin_top = "6rem",
                    rows = [3] #temp
                ),
                rx.box()
            ),

            rows = [3]
        )


