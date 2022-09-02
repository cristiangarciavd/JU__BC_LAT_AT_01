from parser import Parser
from bs4 import BeautifulSoup

class AliParser(Parser):

    def parse(self, page):

        soup = BeautifulSoup(page, "html.parser")

        all_items = soup.find_all("a", {'class':"_3t7zg _2f4Ho"})
        
        amazon_products = []

        for item in all_items:  # create list of dictionaries

            try:
                product = (item.find('h1', class_="_18_85")).get_text()
                price_all = item.find('div', class_ = "mGXnE _37W_B")
                price_items = price_all.find_all('span')
                price = str(price_items[1].get_text())+str(price_items[2].get_text())+str(price_items[3].get_text())
                link_img = "https:" + (item.find("img"))["src"]
                link_url = "https:" + item['href']
                amazon_products.append({
                'product' : product,
                'price' : price,
                'link_img' : link_img,
                'link_url' : link_url,
                'origin' : 'Aliexpress'
                })
            except:
                pass

        return amazon_products