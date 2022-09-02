
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager import chrome
from selenium.webdriver.chrome.options import Options

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


option = Options()
option.headless = True
driver = webdriver.Chrome(options=option)
driver.get(url)
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')
product_name = soup.find_all("h1", attrs={"class": "_18_85"})
product_price = soup.find_all("div", attrs={"class": "mGXnE _37W_B"})
cont = 0
for a in range(len(product_name)):
    cont += 1
    print(product_name[a].text)
    print(product_price[a].text)

print(cont)
