import reflex as rx
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from icecream import ic



Base = declarative_base()



class Product(Base):
    __tablename__ = "products"


    product_name = db.Column("product_name", db.String, primary_key = True)
    sites = db.Column("sites", db.String)
    scrape_results = db.Column("scrape_results", db.VARCHAR(10000))


    def __init__(self, product_name, sites, scrape_results):
        self.product_name = product_name
        self.sites = sites
        self.scrape_results = scrape_results



    def __repr__(self):
        return f"({self.product_name} {self.sites} {self.scrape_results})"



engine = db.create_engine("sqlite:///waveletdb.db", echo = True)
Base.metadata.create_all(bind = engine)


Session = sessionmaker(bind = engine)
session = Session()



def create_entry(product):
    product_name = product["product_name"]
    sites = product["sites"]
    results = product["results"]

    #joining lists, sites and results, together into strings to store in database
    sites = "+++".join(sites)
    results = "+++".join(results)

    session.add(Product(product_name, sites, results))
    session.commit()



def query_database():
     query = session.query(Product.product_name).all()

     return query



def get_scrape_data(productname):
    product = {
        "product_name": productname,
        "sites": [],
        "results": []
    }

    sites = session.query(Product.sites).filter_by(product_name = productname).first()
    results = session.query(Product.scrape_results).filter_by(product_name = productname).first()

    sites = str(sites)
    sites = sites.split("+++")
    sites = " ".join(sites)

    results = str(results)
    results = results.split("+++")
    results = " ".join(results)
    
    
    product["sites"].append(sites)
    product["results"].append(results)

    return product



def delete_product(productname):
    ic(productname)
    product = session.query(Product).filter_by(product_name = productname).first()

    if product:
        session.delete(product)
        session.commit()

        ic(f"Deleted product: {productname}")
    else:
        ic(f"Product: {productname} not found")