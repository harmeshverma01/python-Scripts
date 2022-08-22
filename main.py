
import json
from util.utils import product_details, html_content, get_next_page
url = "https://www.flipkart.com/search?q=mobiles"




soup = html_content(url)
divs = soup.find_all("div",{"class": "_2kHMtA"})

list_of_product = product_details(divs, list_of_product=[])


nextpage = get_next_page(soup)

while True:
    soup = product_details(divs, list_of_product)
    url = get_next_page(soup)
    if not url:
        break
    print(url)

with open('data.json', 'w')as f:
    json.dump(list_of_product, f) 

# with open('data.json', 'w')as f:
#     json_data = json.dumps(list_of_product)
#     print(json_data, 'abcd')
#     json.dump(json_data, f)
# #json.load([list_of_product])        
        