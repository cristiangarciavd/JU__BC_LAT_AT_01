from django.shortcuts import render
import requests

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),' 
)

class Receiver:
    
    def get_products(request): 
        
        response = requests.get('https://6316505533e540a6d391f345.mockapi.io/api/v1/products').json()
        return render(request, 'products.html',{'response':response})
