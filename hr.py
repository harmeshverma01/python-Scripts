#get the html

#print(htmlContent)


#parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

title = soup.title
# print(type(soup))
# print(type(title))
# print(type(title.string))

#Get all the paragraphs from the page

paras = soup.find_all('p')
#print(paras)



#Get Frist element in the html page
#print(soup.find('p')['class'])

#find all the elements using class
#print(soup.find_all("p", class_="lead"))

#get the text from the tags/soup
#print(soup.find('p').get_text())

#print(soup.get_text())

#get all the anchors
anchors = soup.find_all('a')
all_links = set()
#Get all the links on the page
for link in anchors:
    if (link.get('href') != '#'):
        linktext = "https://www.flipkart.com/search?q=mobiles" +link.get('href')
        all_links.add(link)
        #print(linktext)
        
        
markup = "<p><!--this is a comment--></p>"
soup2 = BeautifulSoup(markup, features="html5lib")
#print(type(soup2.p.string))

#.contents = A tag children are avaiable as a list
#.children = A tag's children are avaiavle as a generator

# for elem in container.children:
#     print(elem)

 
# for item in container.stripped_strings:
#     print(item)   

    
# print(soup.find('container'))
# print(soup.fihtml5lib_but_no_id(tag):
#     `return .has_attr('_3HqJxg') and not .has_attr('container')

title = soup.title
print(title)

title = soup.title.name
print(title)

title = soup.title.string
print(title)

title = soup.title.parent.name
print(title)

title = soup.p
print(title)

soup.p['class']

container = soup.find(id="container")

for item in container.strings:
    print(item)   
    
    


def get_page(url):
    response = requests.get("https://www.flipkart.com/search?q=mobiles")

    if not response.ok:
        print('server responded:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup


# pars = div.find('div',{"class": "_3pLy-c"})
# print(pars.text)


# for div in divs[0:2]:
#     paras = div.find('div', {"class" :"_4rR01T"})
#     print(paras.text)    
    