# import requests
# from bs4 import BeautifulSoup
# import json

# url = "https://www.flipkart.com/search?q=mobiles&page=2"


# for page in range(1,300):
#     content = requests.get(url + str(page) + '/')
#     soup = BeautifulSoup(content.text, 'html.parser')
#     title = soup.find_all('div', attrs=({'class': '_1LKTO3'}))

# for i in range(1,300):
#     if page>1:
#         print(f"{(i-3)}+page*10)" + title[i].text)
#     else:
#         print(f'{i-3}' + title[i].text)          
              
# with open('data.json', 'w')as f:
#     json.dump(page, f) 

import requests
from bs4 import BeautifulSoup
url = "https://www.flipkart.com/search?q=mobiles"

def product_details(divs, list_of_product):
    for div in divs:
        product_name = div.find('div', {"class" : "_4rR01T"})
        product_rating = div.find('div', {"class": "_3LWZlK"})
        product_discription = div.find('div',{"class" : "fMghEO"})
        product_price = div.find('div', {"class":"nlI3QM"})
        
        
        product = {
            'name' : product_name.text,
            # 'rating' : product_rating.text,
            'discription' : product_discription.text,
            'price' : product_price.text,
        }
        list_of_product.append(product)
    return list_of_product
        

def html_content(url):
    content = requests.get(url)
    htmlContent = content.content
    soup = BeautifulSoup(htmlContent, 'html5lib')
    return soup


def get_next_page(url):
    soup = html_content(url)
    print(soup)
    nextpage = soup.find('a', {'class' : '_1LKTO3'})
    print("SHJNJN: ", nextpage)
    if not nextpage.find('span',{'class' : '_22Tduf'}):
        url = 'http://www.flipkart.com' + nextpage.attrs['href'] 
        return (url)
    else:
        return
    

    