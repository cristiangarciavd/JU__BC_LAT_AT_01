
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scraper_strategy import ScraperStrategy
from bs4 import BeautifulSoup

class AliexpressScraperStrategy(ScraperStrategy):

    def __init__(self, url) -> None:
        if(url==''):
            raise ValueError(f"Invalid Url: Please digit a valid url")
        else: 
            self.url=url

    def empty_url(self):
        if(self.url):
            return False
        else:
            True

    def get_url(self):
        return self.url

    def get_html(self, url):
        option = Options()
        option.headless = True
        driver = webdriver.Chrome(options=option)
        driver.get(url)
        return driver.page_source
        

class Main:
    def run():
        Scrapper = AliexpressScraperStrategy("https://es.aliexpress.com/af/black-shoe.html?d=y&origin=n&SearchText=black+shoe&catId=0&spm=a2g0o.productlist.1000002.0&initiative_id=SB_20220830102312")
        print(Scrapper.url)
        html = Scrapper.get_html(Scrapper.url)
        print(html)

    if __name__ == "__main__":
        try:
            run()
        except ValueError as ex:
            print(f'\n Something went wrong', {ex})