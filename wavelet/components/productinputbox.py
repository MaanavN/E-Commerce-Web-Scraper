import reflex as rx
from .BaseState import BaseState
from .. import scrape_product
from .productlist import get_product_list
from icecream import ic
import time



#creating state to handle input
class InputState(BaseState):
    text = ""
    processing_request = False

    def get_product(self):
        if len(self.text) > 0 and self.processing_request == False:
            if self.check_counter <= 0:
                self.error_message = "Please check atleast one box."
            else:
                self.processing_request = True
                self.error_message = ""
                


                product = {
                    "product_name": self.text,
                    "sites": [],
                    "results": []
                }

                if self.amazon == True:
                    product["sites"].append("amazon")


                time.sleep(2)
                scrape_product.main(product)

                time.sleep(1)
                self.processing_request = False


                #updating list of product names
                get_product_list()




    #code for the checkboxes for each site
    amazon = False

    check_counter = 0
    error_message = ""
    
    def toggle_amazon(self):
        self.amazon = not self.amazon

        if self.amazon == True:
            self.check_counter += 1
        else:
            self.check_counter -= 1


    #resetting everything to default values
    def reset_self(self):
        self.reset()


    #incase the product already exists within the database
    def change_error_message(self, new_text):
        self.error_message = new_text



#creating input box and enter button
def product_input_box():
    return rx.container(
        rx.vstack(
            rx.box(
                rx.input(
                    value = InputState.text,
                    on_change = InputState.set_text,
                ),
                width = '75%',
                margin_top = "1rem"
            ),
            rx.responsive_grid(
                rx.box(
                    rx.checkbox(
                        "Amazon",
                        color_scheme = "blue",
                        on_change = InputState.toggle_amazon()
                    ),
                    margin_top = "1rem",
                    margin_bottom = "0.25rem"
                )
            ),
            rx.text(
                InputState.error_message,
                color = "rgb(188,188,188)"
            ),
            rx.button(
                "Enter",
                on_click = InputState.get_product
            )
        )
    )