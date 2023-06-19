#requests -> GET, POST, PUT/PATCH, DELETE

import requests

#making a GET Request
r = requests.get('https://lingarajtechhub.com/python-object-oriented-programming/')

print(r) #status code 200

print(r.content)#content display

#Response Object

#Request And Response Object

import requests

r = requests.get('https://lingarajtechhub.com/python-object-oriented-programming/')

print(r.url)

print(r.status_code)


#BeautifulSoup Library 3.0, 2.0 v3 or 4

#Incoming records to Unicode
#Outgoing forms to UTF-8

# python parsers like LXML and HTML

# Python BeautifulSoup Parsing HTML

import requests

from bs4 import BeautifulSoup

r = requests.get('https://lingarajtechhub.com/python-object-oriented-programming/')

print(r)

#Parsing the HTML
soup = BeautifulSoup(r.content,'html.parser')
print(soup.prettify())


import requests
from bs4 import BeautifulSoup

#Make A GET Request
r = requests.get('https://lingarajtechhub.com/python-object-oriented-programming/')

soup = BeautifulSoup(r.content,'html.parser')

print(soup.prettify())

print(soup.title)#title tag

print(soup.title.name)#getting the name of the tag

print(soup.title.parent.name) #getting name of the parent tag


#Finding Elements (.class, #id name) #paragraph
import requests
from bs4 import BeautifulSoup

#Make A GET Request
r = requests.get('https://lingarajtechhub.com/what-is-object-oriented-programming-in-python/')

soup = BeautifulSoup(r.content,'html.parser')

s = soup.find('main',class_='site-main hfeed')

content = s.find_all('p')

print(content)

#Finding Elements (Extract The Links)
import requests
from bs4 import BeautifulSoup

#Make A GET Request
r = requests.get('https://lingarajtechhub.com/what-is-object-oriented-programming-in-python/')

soup = BeautifulSoup(r.content,'html.parser')

s = soup.find('div',class_='hero-section')

content = s.find_all('a')

print(content)


#Finding Elements ("More Links")
import requests
from bs4 import BeautifulSoup

#Make A GET Request
r = requests.get('https://lingarajtechhub.com/what-is-object-oriented-programming-in-python/')

soup = BeautifulSoup(r.content,'html.parser')

s = soup.find('div',class_='hero-section')

for a in s.find_all('a', href=True):
    print("Found the URL:", a['href'])


#Finding Elements ('image src'),image url
import requests
from bs4 import BeautifulSoup

#Make A GET Request
r = requests.get('https://lingarajtechhub.com/what-is-object-oriented-programming-in-python/')

soup = BeautifulSoup(r.content,'html.parser')

s = soup.find('div',class_='ct-image-container')

content = s.find('img')

print(content['src'])


#Finding Elements ('image src download')
import requests
from bs4 import BeautifulSoup

#Make A GET Request
r = requests.get('https://lingarajtechhub.com/what-is-object-oriented-programming-in-python/')

soup = BeautifulSoup(r.content,'html.parser')

s = soup.find('div',class_='ct-image-container')

content = s.find('img')

ig = content['src']

#download the image
img_data = requests.get(ig)
img_data.raise_for_status()

#save the image to an file
with open('ig.jpg', 'wb') as handler: 
    handler.write(img_data.content)


"""
get all the images of a particular web page using the 
coresponding url and the following library
"""

import re #regular expression
import requests
from bs4 import BeautifulSoup

site = 'https://lingarajtechhub.com/python-object-oriented-programming/'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png|webp))$', url)
    if not filename:
         print("Regex didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)


