from parser import Parser
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

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
