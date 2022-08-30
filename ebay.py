import requests
from bs4 import BeautifulSoup
 

item = input("Enter the item you want to search:")
URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw="+item+"&_sacat=0"
r= requests.get(URL)
data = r.text
soup = BeautifulSoup(data)
prod = soup.find_all('li', attrs={'class': 's-item'})
print(prod)