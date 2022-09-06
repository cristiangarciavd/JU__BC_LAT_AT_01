from parser import Parser
from bs4 import BeautifulSoup

class EbayParser(Parser):

    def parse(self, page):

        soup = BeautifulSoup(page, "html.parser")

        ebay_products = []

        all_items = soup.find_all(class_= "s-item s-item__pl-on-bottom")
        
        if len(all_items) == 0:
            all_items = soup.find_all(class_= "s-item__info clearfix")
            
            for item in all_items:  

                try:
                    product = (item.parent.parent.find(class_="s-item__title")).get_text()
                    if product == 'Shop on eBay':
                        continue
                    price = item.parent.parent.find(class_ = "s-item__price").get_text()
                    price = price.replace('USD', '')
                    link_img = (item.parent.parent.find("img"))["src"]
                    link_url = item.parent.parent.find("a")['href']
                    ebay_products.append({
                    "product" : product,
                    "price" : price,
                    "link_img" : link_img,
                    "link_url" : link_url,
                    "origin" : "Ebay"
                    })
                except:
                    pass
            
        for item in all_items:  

            try:
                product = (item.find(class_="s-item__title")).get_text()
                if product == 'Shop on eBay':
                    continue
                price = item.find(class_ = "s-item__price").get_text()
                price = price.replace('USD', '')
                link_img = (item.find("img"))["src"]
                link_url = item.find("a")['href']
                ebay_products.append({
                "product" : product,
                "price" : price,
                "link_img" : link_img,
                "link_url" : link_url,
                "origin" : "Ebay"
                })
            except:
                pass

        return ebay_products