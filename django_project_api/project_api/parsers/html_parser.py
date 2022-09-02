from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
from parser import Parser

class AmazonParser(Parser):

    def parse(self, page):

        soup = BeautifulSoup(page, "html.parser")

        all_items = soup.find_all("div", {'data-component-type':"s-search-result"})

        amazon_products = []

        for item in all_items:  # create list of dictionaries

            try:
                product = (item.find(class_="a-size-base-plus a-color-base a-text-normal")).get_text()
                price = str(item.find("span", {'class' : "a-price-whole"}))+str(item.find(class_="a-price-fraction"))
                price = price.replace('<span class="a-price-decimal">', '')
                price = price.replace('<span class="a-price-whole">', '')
                price = price.replace('<span class="a-price-fraction">', '')
                price = price.replace('</span>', '')

                link_img = (item.find("img"))["src"]
                link_url = "https://www.amazon.com" + item.find("a", class_ = "a-link-normal s-no-outline", href = True)['href']
                amazon_products.append({
                'product' : product,
                'price' : price,
                'link_img' : link_img,
                'link_url' : link_url
                })
            except:
                pass

        return amazon_products


class EbayParser(Parser):

    def parse(self, page):

        soup = BeautifulSoup(page, "html.parser")

        all_items = soup.find_all('li', class_= "s-item s-item__pl-on-bottom")
        
        ebay_products = []

        for item in all_items:  # create list of dictionaries

            try:
                product = (item.find(class_="s-item__title")).get_text()
                if product == 'Shop on eBay':
                    continue
                price = item.find(class_ = "s-item__price").get_text()
                price = price.replace('USD', '')
                link_img = (item.find("img"))["src"]
                link_url = item.find("a")['href']
                ebay_products.append({
                'product' : product,
                'price' : price,
                'link_img' : link_img,
                'link_url' : link_url
                })
            except:
                pass

        return ebay_products


class AliParser(Parser):

    def parse(self, page):

        
        r = page
        product_name=r.html.find('h1._18_85')
        product_price=r.html.find('div._37W_B')
        for i in range(len(product_name)):
            print(product_name[i].text)
            print(product_price[i].text) 
        # all_items = soup.find_all({'class' :'_3t7zg _2f4Ho'})
        # print(all_items)
        # amazon_products = []

        # for item in all_items:  # create list of dictionaries

        #     try:
        #         product = (item.find(class_="a-size-base-plus a-color-base a-text-normal")).get_text()
        #         price = str(item.find("span", {'class' : "a-price-whole"}))+str(item.find(class_="a-price-fraction"))
        #         price = price.replace('<span class="a-price-decimal">', '')
        #         price = price.replace('<span class="a-price-whole">', '')
        #         price = price.replace('<span class="a-price-fraction">', '')
        #         price = price.replace('</span>', '')

        #         link_img = (item.find("img"))["src"]
        #         link_url = "https://www.amazon.com" + item.find("a", class_ = "a-link-normal s-no-outline", href = True)['href']
        #         amazon_products.append({
        #         'product' : product,
        #         'price' : price,
        #         'link_img' : link_img,
        #         'link_url' : link_url
        #         })
        #     except:
        #         pass

        # return amazon_products

# example Amazon
# f = open('example_amazon.html')
# file = f.read()

# example ebay
# URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=camisa+para+hombre&_sacat=0"
# r= requests.get(URL)
# data = r.text

# exmple aliexpress
url = "https://es.aliexpress.com/af/camisa-para-hombre.html?d=y&origin=n&SearchText=camisa+para+hombre&catId=0&spm=a2g0o.best.1000002.0&initiative_id=SB_20220902102307"
s=HTMLSession()
r=s.get(url)
print(r)
# pepe = AliParser()
# my_list= pepe.parse(r)
# print(my_list)
