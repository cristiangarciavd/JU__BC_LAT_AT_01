import unittest

from amazon_scrapper_strategy import AmazonScrapperStrategy


class TestAmazonScrapperStrategy(unittest.TestCase):
    def test_geturl_method(self):
        search_word = 'camisas para hombre'
        amazon_scrap = AmazonScrapperStrategy()
        amazon_scrap.get_url(search_word)
        response = amazon_scrap.read_information()
        self.assertEqual(amazon_scrap.get_url(search_word), response.url)

    def test_response_status(self):
        search_word = 'camisas para hombre'
        amazon_scrap = AmazonScrapperStrategy()
        url = amazon_scrap.get_url(search_word)
        response = amazon_scrap.read_information(url)
        self.assertEqual(response.status_code, 200)

    def test_omit_geturlmethod_call(self):
        search_word = 'camisas para hombre'
        amazon_scrap = AmazonScrapperStrategy()
        response = amazon_scrap.read_information()
        self.assertEqual(response.status_code, 200)