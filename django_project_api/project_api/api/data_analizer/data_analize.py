from ast import parse
from itertools import product
from Scraper.scraper import Scraper
from parsers.parser_factory import ParserFactory

product_name = 'cartitas de pokemon'
pages = ['amazon', 'ebay', 'aliexpress']

pages_scrap = Scraper()
html_content = pages_scrap.scrap(product_name)

parser = ParserFactory()
for page in pages:
    parse_type = parser.parser(page + 'parser')
    parse_type.parse(html_content[page])