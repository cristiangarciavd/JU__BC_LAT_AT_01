from api.scraper.scraper_strategy import ScraperStrategy
import requests

class AmazonScrapperStrategy(ScraperStrategy):
    def __init__(self):
        self.__template = 'https://www.amazon.com/s?k={}'
        self.__headers = {
            'authority': 'www.amazon.com.mx',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,es;q=0.7,es-MX;q=0.6',
            'device-memory': '8',
            'downlink': '5.4',
            'dpr': '1',
            'ect': '4g',
            'referer': 'https://www.amazon.com.mx/ref=nav_logo',
            'rtt': '50',
            'sec-ch-device-memory': '8',
            'sec-ch-dpr': '1',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-viewport-width': '1600',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Safari/537.36',
            'viewport-width': '1600',
        }
        self.url = None

    def __str__(self):
        return "amazon"

    def get_url(self, product_name):
        product_name = product_name.replace(' ', '+')
        self.url = self.__template.format(product_name)
        return self.url

    def read_information(self, product_name):
        url = self.get_url(product_name)

        if url:
            try:
                requests.get(url)
            except Exception:
                raise ValueError('Invalid URL')

            response = requests.get(url, headers=self.__headers)
        else:
            self.get_url("")
            response = requests.get(self.url, headers=self.__headers)
            raise TypeError('Missing search term')
        return response.text
