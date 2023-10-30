from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import os
import re
from icecream import ic
import sys
import time



#temp
try:
    def get_soup(url):
        driver = webdriver.Firefox()
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')


        driver.close()

        return soup



    def get_product_links(soup):
        print(soup.title.text.strip()) #temp
        product_links = []
        for link in soup.find_all('a'):
            try:
                href = link.get("href")

                if f"{str(href)[0]}{str(href)[1]}{str(href)[2]}" == "/ip":
                    product_links.append(href)
            except IndexError:
                pass

        
        return product_links



    def get_names_and_prices(product_links):
        names_and_prices = []
        for link in product_links:
            time.sleep(2)
            soup = get_soup(f"https://www.walmart.com{link}")
            #temp
            ic(f"\n{soup.title.text.strip()}")
            if str(soup.title.text.strip()) != "Robot or human?":
                html = soup.prettify()
                
                name = soup.title.text.strip()
                name = name.split()
                name.pop(-1)
                name.pop(-1)
                name = "".join(name)

                
                price = ""
                for element in soup.find_all('span'):
                    if element.get('aria-hidden') == 'false' and element.get('itemprop') == 'price':
                        price = str(element.text)
                        break
                    

                names_and_prices.append([name, price])
                break #temp


        return names_and_prices



    def main(product):
        product = str(product).split()
        product = "+".join(product)
        
        for i in range(1, 5+1):
            soup = get_soup(f"https://www.walmart.com/search?q={product}")
            product_links = get_product_links(soup)
            names_and_prices = get_names_and_prices(product_links)

            if len(names_and_prices) != 0:
                break
            else:
                if i == 6:
                    names_and_prices = "Problem while scraping, try again later"


        return f"Walmart: {names_and_prices}"

        

except KeyboardInterrupt:
    sys.exit()