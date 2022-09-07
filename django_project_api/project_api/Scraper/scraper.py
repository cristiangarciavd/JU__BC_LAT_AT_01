from amazon_scraper_strategy import ScraperStrategy, AmazonScraperStrategy, AliexpressScraperStrategy
from ebay_scraper import EbayScrapperStrategy


class Scraper:

    def __init__(self):
        self.strategies = [AmazonScraperStrategy(), EbayScrapperStrategy(), AliexpressScraperStrategy()]

    def scrap_page(self, strategy: ScraperStrategy, product) -> {str: str}:
        result = strategy.read_information(product)
        return {str(strategy): result}

    def scrap(self, product) -> [{str: str}]:
        if product != "":
            lst = []
            for s in self.strategies:
                lst.append(self.scrap_page(s, product))
            return lst
        else:
            raise ValueError("There is not a product")




