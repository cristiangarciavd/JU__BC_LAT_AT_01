from parser import Parser
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

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