from scraper_strategy import ScraperStrategy
from amazon_scrapper_strategy import AmazonScrapperStrategy
from ebay_scrapper_strategy import EbayScrapperStrategy
from aliexpress_scrapper_strategy import AliexpressScraperStrategy


class Scraper:

    def __init__(self):
        self.strategies = [AmazonScrapperStrategy(), EbayScrapperStrategy(), AliexpressScraperStrategy()]

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


if __name__ == "__main__":

    scraper = Scraper()
    scrap = scraper.scrap("camisa")
    print(scrap)




