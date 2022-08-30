from bs4 import BeautifulSoup
import requests

def get_url(search_term):
    template = 'https://www.amazon.com.mx/s?k={}&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2KCL0E2N251B&s'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)

url = get_url("camisas nike")
print(url)

my_header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Safari/537.36'}

page = requests.get(url, headers=my_header)

soup = BeautifulSoup(page.content, 'html.parser')

titles = soup.find_all(class_="s-line-clamp-1")
sub_titles = soup.find_all(class_="a-size-base-plus a-color-base a-text-normal")
prices = soup.find_all(class_="a-price-whole")

# for price in prices:
#     price = price.get_text()
#     print(price)

# for title in titles:
#     title = title.get_text()
#     print(title)

for index in range(len(titles)):
    print(titles[index].get_text(), " : ", sub_titles[index].get_text(), ": $", prices[index].get_text().replace(" ", "$"))
