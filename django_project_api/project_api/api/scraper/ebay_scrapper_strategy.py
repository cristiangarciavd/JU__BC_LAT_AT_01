import requests


class EbayScrapperStrategy(ScrapperStrategy):
    def __init__(self) -> None:
        self.url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={}&_sacat=0"

    def __str__(self):
        return "ebay"

    def get_url(self, item):
        item = item.split()
        item = "+".join(item)
        return self.url.format(item)
    
    def read_information(self,item):
        self.url = self.get_url(item)
        r = requests.get(self.url)
        try:
            r.status_code == 200
        except:
            print("Something go wrong")
        self.html = r.text
        return self.html

#x = EbayScrapperStrategy()

#print(x.read_information("camisa para hombre"))
