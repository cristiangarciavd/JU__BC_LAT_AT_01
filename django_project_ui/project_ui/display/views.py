from django.shortcuts import render
import requests
from logger.logger import *

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),' 
)

class Receiver:
    @wrap(entering, exiting)
    def get_products(request): 
        """ Retrieve products from API """
        response = requests.get('https://6316505533e540a6d391f345.mockapi.io/api/v1/products').json()
        return render(request, 'products.html',{'response':response})
