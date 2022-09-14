import unittest
from api.scraper.amazon_scrapper_strategy import AmazonScrapperStrategy

class TestAmazonScrapperStrategy(unittest.TestCase):
    def test_geturl_method(self):
        product_name = 'camisas para hombre'
        amazon_scrap = AmazonScrapperStrategy()
        amazon_scrap.read_information(product_name)
        self.assertEqual(amazon_scrap.url, amazon_scrap.response.url)

    def test_response_status(self):
        product_name = 'camisas para hombre'
        amazon_scrap = AmazonScrapperStrategy()
        response = amazon_scrap.read_information(product_name)
        self.assertEqual(response.status_code, 200)

    def test_readinformation_without_argument(self):
        amazon_scrap = AmazonScrapperStrategy()
        amazon_scrap.read_information()
        self.assertEqual(amazon_scrap.response.status_code, 200)