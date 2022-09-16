from api.scraper.scraper_strategy import ScraperStrategy
import requests
from logger.logger import *

class AmazonScrapperStrategy(ScraperStrategy):
    def __init__(self):
        self.__template = 'https://www.amazon.com/s?k={}'
        self.__headers = {
        'authority': 'www.amazon.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,es;q=0.7,es-MX;q=0.6',
        # Requests sorts cookies= alphabetically
        'cookie': 'ubid-main=134-6077895-9364345; sp-cdn="L5Z9:MX"; session-id=144-2872632-4641420; session-id-apay=144-2872632-4641420; x-main="cmclv?V3kNUaY3TDtRmJn5@YBre@mct2rhyPVBOOsN6N3fBzHZJlPf8ZtFw8I@vA"; at-main=Atza|IwEBICODoRvnt4dwwa1ZjvB2_kWWh0VtdXNqItSMefAGn9TTUg5AdGGb8KIXe0NRKZrpfqgTeIqWC0AFGbDNEOksa4gWSUPgQIqv99HRlTikFsLHDW6AnjuDLYmTiW7poGsyLVHFZCUFfwaEmUXq9cjzc3G-30FeBZKi-zK5VQvqf0VZ_pCVlPiZJDlOQCZrnJ5Ypmdsxg4pSTXpBWY0v44BVVKZ; sess-at-main="ut/0dX1a3KJPrvNWe14y6B9PA476eqeVhprCct2QyEI="; aws-target-data=%7B%22support%22%3A%221%22%7D; regStatus=pre-register; i18n-prefs=USD; aws-target-visitor-id=1661887494841-71749.35_0; s_fid=5D8B6D2B51762160-0899596703A87DB6; session-id-time=2082787201l; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19235%7CMCMID%7C40867391841511465071622547509760865542%7CMCAAMLH-1662577884%7C7%7CMCAAMB-1662577884%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1661980285s%7CNONE%7CMCAID%7C315949A196B8833D-60000530004ED6A6%7CMCSYNCSOP%7C411-19242%7CvVersion%7C4.4.0; lc-main=pt_BR; skin=noskin; session-token="ph8EhspGI+D9mUmCz9ONMozTKcQ5RmOH/4+J4L4ZhdeDjmXrY8dSd//EZMK2KvE6JfjOOvE8D1BzTlVQkgJS//240yExs1VJCMIgs6W9Ue091sxCGPSBjBOne4YZH79aeFEck6KAIN3majx0n6Q8Uz0VaNuY/2Pfgfg2nF3VzEIrqh/jjE2764QBrC0ckeEMTii/Vxq4ViulzJyv6IFipow2AP7GBX9g5iJ9UoScm9RIP0SVpK5PbQ=="; csm-hit=adb:adblk_no&t:1663283412478&tb:CJ35R8Z8X2NS1Z26A9BA+s-KK77P7M2X809WP7Q96TP|1663283412478',
        'device-memory': '8',
        'downlink': '10',
        'dpr': '1',
        'ect': '4g',
        'referer': 'https://www.amazon.com/s?k=teclado&crid=3MXBSWS1Z1PGW&sprefix=%2Caps%2C99&ref=nb_sb_ss_recent_1_0_recent',
        'rtt': '50',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '1',
        'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-viewport-width': '1600',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'viewport-width': '1600',
        }
        self.url = None
        
    def __str__(self):
        return "amazon"

    @wrap(entering, exiting)
    def get_url(self, product_name):
        """Geting Amazon url"""
        product_name = product_name.replace(' ', '+')
        url = self.__template.format(product_name)
        return url

    @wrap(entering, exiting)
    def read_information(self, product_name):
        """Scraping Amazon"""
        self.url = self.get_url(product_name)
           
        if self.url:
            try:
                response = requests.get(self.url, headers=self.__headers)
                while str(product_name) not in (response.text):
                    
                    response = requests.get(self.url, headers=self.__headers)
            except Exception:
                
                raise ValueError('Invalid URL')

        else:
            
            raise TypeError('Missing search term')
        
        return response.text
