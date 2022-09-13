import re
from api.scraper.scraper import Scraper
from api.parser.parser_factory import ParserFactory

class DataCollector():
    def __init__(self):
        self.product_name = 'iphone X' #iphone X no funciona para amazon
        self.pages = []
        self.pages_id = {}
        self.__pages_products = [] # unsorted products list
        self.__sorted_products = [] #products sorted in some way
        self.__page_parser = ParserFactory()
        self.__web_scrapper = Scraper()

    def __scrap_html_contents(self, product_name):
        self.product_name = product_name
        self.__html_contents = self.__web_scrapper.scrap(product_name)
        for page_dict in self.__html_contents: #Page names retrieval from html contents -> [{'amazon':htmlcontent},{'ebay':htmlcontent}...])
            for key in page_dict.keys():
                self.pages.append(key)
        for idx, page in enumerate(self.pages): self.pages_id[page] = idx #adjudicating an index to a page.['amazon': 0, 'ebay': 1, ...]

    def __parse_data(self):
        for idx, page in enumerate(self.pages):
            parse_type = self.__page_parser.parser(page + "parser")
            self.__pages_products.append(parse_type.parse(self.__html_contents[idx][page])) # pages_products = [[{p1},{p2},{p3}],[{p1},{p2}...],...]


    def sort_by_price(self, reverse = False):
        self.__sorted_products.clear()
        for products in self.__pages_products:
            self.__sorted_products.append(sorted(products, key=lambda x: float(x['price']), reverse=reverse))
        return self.__sorted_products 

    def price_validation(self, products):
        invalid_price_products = []
        pattern = re.compile(r"\d{1,3}[\s\,\d]\d{1,3}[\s\,\d]\d{1,3}\.\d{1,3}|\d{1,3}\.\d{1,3}|\d{1,3}[\s\,\d]\d{1,3}\.\d{1,3}")
        for product in products[:]:
            matches = pattern.findall(product['price'])
            if matches:
                matches = matches[0].replace('\xa0', "")
                matches = matches.replace(',', "")
                product['price'] = matches
            else:
                invalid_price_products.append(product)
                products.remove(product)

    def collect(self, product_name):
        self.__scrap_html_contents(product_name)
        self.__parse_data()
        for products in self.__pages_products: #To do: Must implement price validation in parsers files
            self.price_validation(products)

    def top_x_products(self, x = 'all'):
        top_products = []
        for idx, products in enumerate(self.__sorted_products):
            top_page_products = []
            if x == 'all':
                return self.__sorted_products
            elif x > len(products) and x > 0: #Need to be upgraded
                print(self.pages[idx] + " store have " + str(len(products)) + " products to offer")
                for idx in range(x):
                    top_page_products.append(products[idx])
            else:
                for idx in range(x):
                    top_page_products.append(products[idx])
            top_products.append(top_page_products)
        return top_products
        

# instance = DataCollector()
# instance.collect('camisas para hombre')
# instance.sort_by_price()
# list = instance.top_x_products(5)
# for page in list:
#     for product in page:
#         print(product['product'], ":", product['price'], product['origin'])
