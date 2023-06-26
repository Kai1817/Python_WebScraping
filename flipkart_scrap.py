"""we are supposed to do the web scrapping before that we need to go through the pages.
i have selected mobile phones of samsung that are above thirty thousand.
This consist of total 23 pages.
i will be scrapping here the datas of each of the phones from all the 23 pages. 
the process goes like this."""

"""getting the url and finding the text inside that particular page related to that url.
we are already in the first page."""

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=mobiles+above+30000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&page=1"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text,'html.parser') 
print(soup) 

""" getting the link for the next page as we have already got the link for 1st page"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=mobiles+above+30000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&page=1"
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser') 
new_page = soup.find("a",class_ = "_1LKTO3").get('href')
tap = "https://www.flipkart.com" + new_page
print(tap)


#url for all those pages we want to do the web scrapping

import pandas as pd
import requests
from bs4 import BeautifulSoup


for i in range(2,25): #number of pages you want to scrap the data from 
    try:
        url = "https://www.flipkart.com/search?q=mobiles+above+30000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&page=" + str(i)
        r = requests.get(url)
        soup = BeautifulSoup(r.text,'html.parser') 
        new_page = soup.find("a",class_ = "_1LKTO3").get('href')
        tap = "https://www.flipkart.com" + new_page
        print(tap)
    except requests.exceptions.RequestException as e:
        print("Error occurred while requesting the page:", e)

print()
print("got all the urls from which data is to be scrapped.")

#scrapping datas of samsung mobile more than 30 thousand from page 1 only out of 23.

import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_Name = []
Prices = []
Description = []
Reviews = []

try:
    url = "https://www.flipkart.com/search?q=mobiles+above+30000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&page=1"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    particular = soup.find('div',class_ = "_1YokD2 _3Mn1Gg")

    n_o_p = particular.find_all('div',class_ = '_4rR01T')  #getting the name of the products only and adding it in an 
    for i in n_o_p:                                       #empty list Product_Name,which will be easy for us to sort the data.
        n = i.text                                
        Product_Name.append(n)                    
    print(Product_Name)
    print()
    print(len(Product_Name))  #to check the number of products name

    print()

    get_price= particular.find_all('div',class_ ='_30jeq3 _1_WHN1')   #getting the prices of the corresponding products and 
    for i in get_price:                                               #sorting it in an empty list Prices.
        n = i.text
        Prices.append(n)
    print(Prices)
    print()
    print(len(Prices))   #to check the number of prices

    print() 

    get_desc = particular.find_all('ul', class_ = '_1xgFaf')     #getting description of the Products and sorting it an
    for i in get_desc:                                           #empty list Description
        n = i.text
        Description.append(n)
    print(Description)
    print()
    print(len(Description))  #to check the number of Description.

    print()

    o_p_r = particular.find_all('div','_3LWZlK')    #getting the reviews of the product and sorting it in an empty list
    for i in o_p_r:                                 # of Reviews 
        n = i.text
        Reviews.append(n)
    print(Reviews)
    print()
    print(len(Reviews))

except requests.exceptions.RequestException as e:
    print("Error occurred while requesting the page:", e)
print()
print("data scraped  for a single page.")

""" Note : we are continously checking the length of the each products, and their corresponding prices,
Description, and the Reviews just to make sure that the we are doing the scrapping in a right way
for all the 24 products that are present in the 1st page."""



##scrapping datas of samsung mobile more than 30 thousand from all the 23 pages.

import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_Name = []
Prices = []
Description = []
Reviews = []

for i in range(2, 25):  #for the number of pages we want to scrap the data.
    try:
        url = "https://www.flipkart.com/search?q=mobiles+above+30000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&page=" + str(i)
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for non-2xx response codes
        soup = BeautifulSoup(r.text, 'html.parser')
        particular = soup.find('div', class_="_1YokD2 _3Mn1Gg")

        n_o_p = particular.find_all('div', class_='_4rR01T')
        for i in n_o_p:
            n = i.text
            Product_Name.append(n)

        get_price = particular.find_all('div', class_='_30jeq3 _1_WHN1')
        for i in get_price:
            n = i.text
            Prices.append(n)

        get_desc = particular.find_all('ul', class_='_1xgFaf')
        for i in get_desc:
            n = i.text
            Description.append(n)

        o_p_r = particular.find_all('div', '_3LWZlK')
        for i in o_p_r:
            n = i.text
            Reviews.append(n)

        if len(o_p_r) < len(n_o_p):
            missing_reviews = len(n_o_p) - len(o_p_r)
            for _ in range(missing_reviews):
                Reviews.append("No reviews available")
    except requests.exceptions.RequestException as e:
        print("Error occurred while requesting the page:", e)

df = pd.DataFrame({"Products": Product_Name, "Prices": Prices, "Description": Description, "Reviews": Reviews})

df.to_csv("E:/python programs/Python_Project/Samsung_phones_above_30K.csv")

print("Data scraping and CSV export completed successfully.")



""" This concludes the scraping of  datas for Samsung Mobiles above 30 thousand price From 
Flipkart website."""
    