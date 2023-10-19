from . import amazon_scraper
from icecream import ic
import sqlalchemy
import models
from .components import productinputbox



def main(product):
    for site in product["sites"]:
        for i in range(1, 5+1):
            if site == "amazon":
                result = amazon_scraper.main(product["product_name"])

                ic(f"{result} {len(result)}") #temp
                
                if len(result) > 10:
                    product["results"].append(result)
                    break
                elif i == 5:
                    ic("Failure") #temp
                else:
                    pass



    try:
        models.create_entry(product)

        #making sure of the same item doesn't get added again
    except sqlalchemy.exc.IntegrityError:
        ic("Item already exists within the database") #temp
        pass
    except sqlalchemy.exc.PendingRollbackError:
        ic("Item already exists within the database")
        pass