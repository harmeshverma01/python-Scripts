import json
from db import get_database
from util.utils import product_details, html_content, get_next_page

db = get_database()
product_coll = db['products']

url = "https://www.flipkart.com/search?q=mobiles"

soup = html_content(url)


while True:
    divs = soup.find_all("div",{"class": "_2kHMtA"})
    list_of_product = product_details(divs, list_of_product=[])
    if list_of_product:
        product_coll.insert_many(list_of_product)
    url = get_next_page(url)
    if not url:
        break
    soup = html_content(url)
    
    # with open('data.json', 'a')as f:
    #     json.dump(collenction_data, f)
        