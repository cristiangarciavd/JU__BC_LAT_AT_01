from django.shortcuts import render
from django.http import HttpResponse
import requests

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),' 
)
 
def index(request):
        return render(request, 'home.html')

class Receiver:
    def get_products(request): 
        response = requests.get('https://6316505533e540a6d391f345.mockapi.io/api/v1/products').json()
        return render(request, 'products.html',{'response':response})
