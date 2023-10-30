from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import os
import re



def get_soup(url):
    driver = webdriver.Firefox()
    #making sure of no error page
    while True:
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        html = soup.prettify()

        if soup.title == "<title>Sorry! Something went wrong!</title>":
            pass
        else:
            break


    driver.close()

    return soup



def collect_search_results(product):
    #replacing spaces with "+" for url
    product = product.split()
    product = "+".join(product)

    soup = get_soup(f"https://www.amazon.com/s?k={product}")
    
    #creating search term for product
    product = product.split("+")
    product = "\+".join(product)

    results = []
    search_term = re.compile(fr"\b\w*{product}\w*\b")

    #search html for all <span> containing product name and adding it to list
    for element in soup.find_all('span'):
        element_split = str(element).split("\"")
        for line in element_split:
            if search_term.search(line) != None:
                results.append(line)
            else:
                pass


    return results



def filter_results(results, product):
    filtered_results = []

    for result in results:
        result = str(result).split("=%7B%")
        filtered_results.append(result)

    name_and_price = []

    product = product.split()
    product = "\\+".join(product)

    search_term = re.compile(fr"\b\w*{product}\w*\b")

    for result in filtered_results:
        result = str(result).split("%22")

    
        try:
            #sorting through every item in result and appending name and price to list
            for j in range(30, 35+1):
                if search_term.search(str(result[j])) != None:
                    price_search_term = re.compile(r"\bamount\b")
                    for i in range(0, 50+1):
                        try:
                            if price_search_term.search(result[i]) != None:
                                #getting the price out of %3A{PRICE}%2C
                                price = str(result[i+1])
                                price = price.split("%3A")
                                price = str(price[1]).split("%2C")
                                price = f"${price[0]}"

                                name = str(result[j]).split("+")

                                #getting rid of unwanted characters. ex: %3A
                                unwanted_characters = re.compile(r"\b\%\w\w\b")
                                try:
                                    for y in range(0, 50+1):
                                        if unwanted_characters.search(name[y]) != None:
                                            name.pop(y)
                                except IndexError:
                                    pass
                                name = " ".join(name)

                                #getting rid any additional reacurring unwanted characters that are part of whole words
                                name = name.replace("%27", "'")
                                name = name.replace("%26", "")
                                name = name.replace("%28", "")
                                name = name.replace("%C2%A0", "")
                                name = name.replace("%2C", "")
                                name = name.replace("16%5C", "")
                                name = name.replace("%2B", "")
                                name = name.replace("%2F", "-")
                                name = name.replace("%E", "")
                                name = name.replace("%80%", "")

                                name_and_price.append([name, price])
                        except ValueError:
                            pass
                else:
                    pass
        except IndexError:
            pass


    return name_and_price



def main(product):
    for i in range(1, 5+1):
        results = collect_search_results(product)
        name_and_price = filter_results(results, product)

        if len(name_and_price) != 0:
            break
        else:
            if i == 6:
                name_and_price = "Problem while scraping, try again later."

    return f"Amazon: {name_and_price}"