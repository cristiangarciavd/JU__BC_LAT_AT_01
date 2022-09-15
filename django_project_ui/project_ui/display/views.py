from django.shortcuts import render
import requests
from logger.logger import *

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),' 
)

from django.shortcuts import render
from django.http import HttpResponse
import requests

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),' 
)
 
def index(request):
        return render(request, 'home.html')

class Receiver:

    @wrap(entering, exiting)
    def get_products(request): 
        """ Retrieve products from API """
        if request.GET.get('search_product'):
            search_product=request.GET.get('search_product')
            url = 'http://127.0.0.1:8000/api/product/'+search_product
            response = requests.get(url).json()
        else:
            response = None
        
        return render(request, 'products.html',{'response':response})

