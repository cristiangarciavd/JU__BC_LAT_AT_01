import requests

class EbayScrapperStrategy():
    def __init__(self, item) -> None:
        self.item = item
    
    def GetURL(self):
        item = self.item.split()
        item = "+".join(item)
        self.URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw="+item+"&_sacat=0"
        return self.URL
    
    def GetHtml(self,URL):
        r = requests.get(self.URL)
        self.html = r.text
        return self.html
