from bs4 import BeautifulSoup
import requests

def get_url(search_term):
    template = 'https://www.amazon.com/s?k={}'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)

url = get_url(input())

headers = {
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


response = requests.get(url, headers=headers)
print(response.url)
print(response.status_code)
#print(response.text)


#Beautiful Soup object represents the document as a nested data structure
soup = BeautifulSoup(response.content, 'html.parser')

#search by CSS class using the keyword argument class_
titles = soup.find_all(class_="s-line-clamp-1")
print("titles:", type(titles[0]))
sub_titles = soup.find_all(class_="a-size-base-plus a-color-base a-text-normal")
print("sub_titles:", len(sub_titles))
prices = soup.find_all(class_="a-price-whole")
print("prices:", len(prices))

print("------Top 10 Products-----")
for index in range(10):
    print(" : ", sub_titles[index].get_text(), ": $", prices[index].get_text())
