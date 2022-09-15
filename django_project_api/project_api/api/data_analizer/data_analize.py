from api.scraper.scraper import Scraper
from api.parser.parser_factory import ParserFactory

class DataCollector():
    def __init__(self):
        self.product_name = 'camisas' #iphone X no funciona para amazon
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
        for single_page_products in self.__pages_products: #iterar hasta que sirva.
            if len(single_page_products) == 0:
                #logger recompilando datos
                self.__html_contents.clear()
                self.__pages_products.clear()
                self.__html_contents = self.__web_scrapper.scrap(self.product_name)
                self.__parse_data()

    def sort_by_price(self, reverse = False):
        self.__sorted_products.clear()
        for products in self.__pages_products:
            self.__sorted_products.append(sorted(products, key=lambda x: float(x['price']), reverse=reverse))
        return self.__sorted_products 

    def collect(self, product_name):
        self.__scrap_html_contents(product_name)
        self.__parse_data()

    def top_x_products(self, x = 'all'):
        top_products = []
        for idx, products in enumerate(self.__sorted_products):
            top_page_products = []
            if x == 'all':
                return self.__sorted_products
            elif x > len(products) and x > 0:
                print(self.pages[idx] + " store have " + str(len(products)) + " products to offer")
                try:
                    for idx in range(x):
                        top_page_products.append(products[idx])
                except:
                    pass
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
