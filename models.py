import boto3
import ctypes
from icecream import ic
from dotenv import load_dotenv
import os



load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")



session = boto3.Session(
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name = AWS_DEFAULT_REGION
)



dynamodb = session.resource('dynamodb')
table = dynamodb.Table('WaveletDB')



def create_entry(product):
    product_name = str(product["product_name"])
    sites = str(product["sites"])
    results = str(product["results"])


    # Creating Entry in DB
    table.put_item(
        Item = {
            "product_name": product_name,
            "sites": sites,
            "results": results
        }
    )


    with open("product_names.txt", "a") as file:
        file.write(f"{product_name}\n")



def query_database(product_name):
    response = table.get_item(
        Key = {
            "product_name": product_name
        }
    )
    product = response["Item"]

    
    return product



def delete_product(product_name):
    table.delete_item(
        Key = {
            "product_name": product_name
        }
    )

    with open("product_names.txt", "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

        for line in lines:
            if str(line) == product_name:
                lines.remove(str(line))

    libc = ctypes.CDLL(None)
    libc.unlink(b"product_names.txt")
    
    with open('product_names.txt', 'a') as file:
        for line in lines:
            file.write(f"{line}\n")