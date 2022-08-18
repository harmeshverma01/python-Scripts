import requests
from bs4 import BeautifulSoup
import json
url = "https://www.flipkart.com/search?q=mobiles"


content = requests.get(url)
htmlContent = content.content


soup = BeautifulSoup(htmlContent, 'html5lib')

list_of_product = []

divs = soup.find_all("div",{"class": "_2kHMtA"})


for div in divs:
    product_name = div.find('div', {"class" : "_4rR01T"})
    product_rating = div.find('div', {"class": "_3LWZlK"})
    product_discription = div.find('div',{"class" : "fMghEO"})
    product_price = div.find('div', {"class":"nlI3QM"})
    
    
    product = {
        'name' : product_name.text,
        'rating' : product_rating.text,
        'discription' : product_discription.text,
        'price' : product_price.text
    }


    list_of_product.append(product)

with open('data.json', 'w')as f:
    json.dump(list_of_product, f) 
