from requests_html import HTMLSession
from bs4 import BeautifulSoup

search = input('Enter the product: ')
splitted = search.split()
if (len(splitted) == 1):
    url = "https://es.aliexpress.com/af/"+search+".html?d=y&origin=n&SearchText=" + \
        search+"&catId=0&spm=a2g0o.productlist.1000002.0&initiative_id=SB_20220830102312"

elif (len(splitted) > 1):
    link1 = ''
    link2 = ''
    minus = 1
    for i in splitted:
        if minus < len(splitted):
            link1 = link1+i+'-'
            link2 = link2+i+'+'
        else:
            link1 = link1+i
            link2 = link2+i
        minus += 1
    url = "https://es.aliexpress.com/af/"+link1+".html?d=y&origin=n&SearchText=" + \
        link2+"&catId=0&spm=a2g0o.productlist.1000002.0&initiative_id=SB_20220830102312"

s=HTMLSession()
r=s.get(url)
r.html.render(timeout=10000)

product_name=r.html.find('h1._18_85')
product_price=r.html.find('div._37W_B')
for i in range(len(product_name)):
    print(product_name[i].text)
    print(product_price[i].text) 