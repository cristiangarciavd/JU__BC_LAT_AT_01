from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from api.scraper.scraper_strategy import ScraperStrategy


class AliexpressScraperStrategy(ScraperStrategy):

    def __str__(self):
        return "aliexpress"

    def get_url(self, item):
        splitted = item.split()
        if len(splitted) == 1:
            url = "https://es.aliexpress.com/af/" + item + ".html?d=y&origin=n&SearchText=" + \
                  item + "&catId=0&spm=a2g0o.productlist.1000002.0&initiative_id=SB_20220830102312"
        elif len(splitted) > 1:
            link1 = ''
            link2 = ''
            minus = 1
            for i in splitted:
                if minus < len(splitted):
                    link1 = link1 + i + '-'
                    link2 = link2 + i + '+'
                else:
                    link1 = link1 + i
                    link2 = link2 + i
            minus += 1
            url = "https://es.aliexpress.com/af/" + link1 + ".html?d=y&origin=n&SearchText=" + \
                  link2 + "&catId=0&spm=a2g0o.productlist.1000002.0&initiative_id=SB_20220830102312"
        return url

    def read_information(self, item):
        if item == '':
            raise ValueError(f"Invalid item: Please digit a valid item")
        else:
            url = self.get_url(item)
            option = Options()
            option.headless = True
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
            driver.get(url)
            return driver.page_source
