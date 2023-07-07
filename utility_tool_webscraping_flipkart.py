"""so basically here we are trying to construct a tool using python codes.

what the tool exactly does is if we give any user input of a product name,it will scrap the
datas of all the related products based on that product name and show us the result
in the python console.

The online website over which the scraping is done is flipkart.

input- enter any flipkart product name.
output - get results related to that product like(product_name,price,description,reviews)  """

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def validate_input(goods_name):
    # Remove leading/trailing whitespaces
    goods_name = goods_name.strip()

    # Check if the input contains only alphanumeric characters and spaces
    if not re.match("^[a-zA-Z0-9 ]*$", goods_name):
        raise ValueError("Invalid input. Only alphanumeric characters and spaces are allowed.")

    return goods_name

def scrape_flipkart_product(goods_name):
    Product_Name = []
    Prices = []
    Description = []
    Reviews = []

    page = 1
    while True:
        try:
            url = f"https://www.flipkart.com/search?q={goods_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page={page}"
            r = requests.get(url, timeout=15)
            r.raise_for_status()  # Raise an exception if request fails
            soup = BeautifulSoup(r.text, 'html.parser')
            particular = soup.find('div', class_="_1YokD2 _3Mn1Gg")

            if particular is None:
                break

            n_o_p = particular.find_all('a', class_='s1Q9rs') or particular.find_all('div', class_='_2WkVRV') or particular.find_all('div', class_='_4rR01T') or particular.find_all('a', class_='IRpwTa')
            for item in n_o_p:
                n = item.text
                Product_Name.append(n)

            get_price = particular.find_all('div', class_='_30jeq3') or particular.find_all('div', class_='_1vC4OE') or particular.find_all('div', class_='_30jeq3 _1_WHN1')
            for item in get_price:
                n = item.text
                Prices.append(n)

            get_desc = particular.find_all('div', class_='_3Djpdu') or particular.find_all('a', class_='_2mylT6') or particular.find_all('div', class_='_3eWWd-') or particular.find_all('ul', class_='_1xgFaf') or particular.find_all('a', class_='IRpwTa')
            for item in get_desc:
                n = item.text
                Description.append(n)

            o_p_r = particular.find_all('div', class_='_3LWZlK') or particular.find_all('div', class_='_2_R_DZ')
            for item in o_p_r:
                n = item.text
                Reviews.append(n)

            next_button = particular.find('a', class_="_1LKTO3")
            if not next_button:
                break

            page += 1

        except requests.exceptions.RequestException as e:
            print("Error occurred while requesting the page:", e)
            break
        except Exception as e:
            print("An error occurred:", e)
            break

    max_length = max(len(Product_Name), len(Prices), len(Description), len(Reviews))
    fill_value = 'not available'

    # Extend lists to have the same length
    Product_Name += [fill_value] * (max_length - len(Product_Name))
    Prices += [fill_value] * (max_length - len(Prices))
    Description += [fill_value] * (max_length - len(Description))
    Reviews += [fill_value] * (max_length - len(Reviews))

    # Create DataFrame
    data = {
        'Product Name': Product_Name,
        'Price': Prices,
        'Description': Description,
        'Reviews': Reviews
    }
    df = pd.DataFrame(data)

    return df

goods_name = input("Enter the product you want to search for: ")
try:
    validated_goods_name = validate_input(goods_name)
    df = scrape_flipkart_product(validated_goods_name)
    if df.empty:
        print("No results found for the given product.")
    else:
        print(df)
        print()
        """after searching the products name,you get the desired results
        If you want to save the product's details that you have got in the result
        in the form of a csv file then
        just remove the undermentioned comment tag over the line and execute the code."""

        #df.to_csv("E:/python programs/Python_Project/product_details.csv")
        print("Scraping done.")
except ValueError as e:
    print("Input validation error:", e)







