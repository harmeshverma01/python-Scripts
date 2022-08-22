import json
from util.utils import product_details, html_content, get_next_page
url = "https://www.flipkart.com/search?q=mobiles"

soup = html_content(url)


while True:
    divs = soup.find_all("div",{"class": "_2kHMtA"})
    list_of_product = product_details(divs, list_of_product=[])
    url = get_next_page(url)
    if not url:
        break
    soup = html_content(url)
    print(url)

    with open('data.json', 'a')as f:
        json.dump(list_of_product, f) 

      
        