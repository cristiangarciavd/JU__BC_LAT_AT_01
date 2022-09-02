from parser import Parser
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

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