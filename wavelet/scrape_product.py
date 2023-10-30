from . import amazon_scraper, walmart_scraper
from icecream import ic
import sqlalchemy
import models
from .components import productinputbox



def main(product):
    for site in product["sites"]:
        if site == "amazon":
            result = amazon_scraper.main(product["product_name"])

            ic(f"{result} {len(result)}") #temp
            
            if len(result) > 15:
                product["results"].append(result)
            else:
                pass
            
        elif site == "walmart":
            result = walmart_scraper.main(product["product_name"])

            ic(f"{result} {len(result)}") #temp
            
            if len(result) > 15:
                product["results"].append(result)
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