Overview
Prerequisites:
-Python3.8+
-requests(library)
-bs4, BeautifulSoap(library)

amazon_scrap.py file has a function 'get_url()' in wich the input is a string and returns a formated string
replicating the URL string format of amazon.

The second funcionality is to request the HTML page content of the URL given, and with use of the find_all() method of the BeautifulSoup library 
search for specific information of the page: Title, description and prices of products.
